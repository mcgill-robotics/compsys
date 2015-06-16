# -*- coding: utf-8 -*-

"""McGill Robotics ROS Bag Merger.

This tool merges all bags in the specified directory that were split by
`bag record`.

By default, all topics defined in your project's 'topics' will be merged if no
arguments are given. Otherwise, only the topics specified will be merged.
"""

import os
import re
import rosbag

__author__ = "Anass Al-Wohoush"


class Merge(object):

    """Merge topics from split bags.

    Attributes:
        topics: List of topics to merge.
        name: Name of bag.
        dir: Path to bags.
        bags: List of split bags in folder.
        output: Merged bag file.
    """

    # Parsing conditions.
    prefix = "split_"
    extension = ".bag"

    def __init__(self, topics, name, dir, args):
        """Construct Merge object.

        Args:
            topics: List of topics to merge.
            name: Name of bag.
            dir: Path to bags.
            args: Additional arguments.
        """
        self.name = name
        self.topics = [topic for elem in topics for topic in elem.topics]
        self.dir = dir
        self.bags = []
        self.output = None

    @staticmethod
    def bag_number(bag):
        """Return bag number.

        Args:
            bag: Bag's filename.

        Returns:
            An integer consisting of the bag's number.
            For example, a bag named 'split_17.bag' would have returned the
            number 17.
        """
        return int(re.findall("\d+", bag)[0])

    def get_bags(self):
        """Get sorted bags to merge from current directory."""
        def is_bag(filename):
            starts_correctly = filename.startswith(Merge.prefix)
            ends_correctly = filename.endswith(Merge.extension)
            corrupt = ("orig" in filename or "active" in filename)

            return (starts_correctly and ends_correctly and not corrupt)

        for (dirpath, dirs, files) in os.walk(self.dir):
            bags = [
                filename for filename in files
                if is_bag(filename)
            ]
            break

        return sorted(bags, key=Merge.bag_number)

    def append(self, bag):
        """Append topics from input bag to output bag.

        Args:
            bag: Path to bag to append.

        Raises:
            rosbag.ROSBagUnindexedException: Bag is unindexed.
        """
        try:
            current = rosbag.Bag(bag, 'r')
            for topic, msg, time in current.read_messages(topics=self.topics):
                self.output.write(topic, msg, time)
        except rosbag.ROSBagUnindexedException:
            print("'{bag}' unindexed".format(bag=bag))
            print("run 'rosbag reindex {bag}' and try again".format(bag=bag))
            raise rosbag.ROSBagUnindexedException
        finally:
            current.close()

    def run(self):
        """Merge all bags to output bag."""
        # Get bags.
        self.bags = self.get_bags()

        # Create and name output bag.
        name = self.name
        while not name:
            name = raw_input("name me: ")
        path = "{dir}/{name}.bag".format(
            dir=self.dir,
            name=name
        )

        print("merging to {bag}".format(bag=path))

        self.output = rosbag.Bag(path, 'w')

        # Merge and close.
        status = 0
        try:
            for bag in self.bags:
                print("merging {} of {}".format(
                    Merge.bag_number(bag) + 1,
                    Merge.bag_number(self.bags[-1]) + 1
                ))
                self.append(bag)
        except rosbag.ROSBagUnindexedException:
            status = 1
        finally:
            self.output.close()
            return status
