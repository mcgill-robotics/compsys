#!/usr/bin/env python

"""Bag merging manager."""

import re
import os
import sys
import rosbag
from Shortcuts import Shortcuts
from Topics import TopicList


class Merger(object):

    """Merge specified topics from bags."""

    # PARSING CONDITIONS
    prefix = "split_"
    extension = ".bag"

    def __init__(self, arg, robot, folder):
        """Construct Bagger object and bag specified topics.

        :param arg: command-line arguments
        :type arg: list of strings
        :param robot: robot name
        :type robot: str
        :param folder: path to folder containing bags
        :type folder: str
        """
        self.arg = arg
        topics_file = '{}/{}.topics'.format(os.path.dirname(__file__), robot)
        all_topics = TopicList(topics_file).topics
        self.enabled = Shortcuts(arg, all_topics, 'merge_bag').enabled
        enabled_topics = (' '.join(elem.topics) for elem in self.enabled)
        self.topics = ' '.join(enabled_topics)
        self.folder = folder
        self.bags = []
        self.output = None

    @staticmethod
    def bag_number(bag):
        """Return bag number."""
        return int(re.findall('\d+', bag)[0])

    def get_bags(self):
        """Get sorted bags to merge from current directory."""
        def is_bag(filename):
            starts_correctly = filename.startswith(Merger.prefix)
            ends_correctly = filename.endswith(Merger.extension)
            corrupt = ("orig" in filename or "active" in filename)

            return (starts_correctly and ends_correctly and not corrupt)

        for (dirpath, dirs, files) in os.walk(self.folder):
            bags = [
                filename for filename in files
                if is_bag(filename)
            ]
            break

        return sorted(bags, key=Merger.bag_number)

    def append(self, bag):
        """Append topics from inpout bag to output bag.

        :param bag: path to bag
        :type bag: str

        :raises rosbag.ROSBagUnindexedException: if bag is unindexed
        """
        try:
            current = rosbag.Bag(bag, 'r')
            for topic, msg, time in current.read_messages(topics=self.topics):
                self.output.write(topic, msg, time)
        except rosbag.ROSBagUnindexedException:
            print "'{bag}' unindexed".format(bag=bag)
            print "run 'rosbag reindex {bag}' and try again".format(bag=bag)
            raise rosbag.ROSBagUnindexedException
        finally:
            current.close()

    def merge(self):
        """Merge all bags to output bag."""
        # GET BAGS
        self.bags = self.get_bags()

        # CREATE AND NAME OUTPUT BAG
        name = None
        while not name:
            name = raw_input("name me: ")
        path = "{folder}/{name}.bag".format(
            folder=self.folder,
            name=name
        )
        self.output = rosbag.Bag(path, 'w')

        # MERGE AND CLOSE
        status = 0
        try:
            for bag in self.bags:
                print 'merging {} of {}'.format(
                    Merger.bag_number(bag) + 1,
                    Merger.bag_number(self.bags[-1]) + 1
                )
                self.append(bag)
        except rosbag.ROSBagUnindexedException:
            status = 1
        finally:
            self.output.close()
            sys.exit(status)


if __name__ == '__main__':
    try:
        robot = os.environ["ROBOT"]
        merger = Merger(sys.argv, robot, '.')
        merger.merge()
    except KeyError:
        print "E: 'ROBOT' variable not exported properly"
        sys.exit(2)
