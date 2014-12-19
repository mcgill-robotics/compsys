#!/usr/bin/env python

"""This script bags the specified topics and splits them every 15 seconds.
By default, all topics defined in your team's '.topics' will be bagged if no
arguments are given. Otherwise, only the topics specified will be bagged."""

__author__ = "Anass Al-Wohoush"
__version__ = '0.9'

import os
import sys
from datetime import datetime
from shlex import split
from Shortcuts import Shortcuts
from Topics import TopicList
from subprocess import Popen


class Bagger(object):

    """Bag specified topics."""

    def __init__(self, arg, robot):
        """Construct Bagger object and bag specified topics.

        :param arg: command-line arguments
        :type arg: list of str
        :param robot: robot name
        :type robot: str
        """
        self.arg = arg
        topics_file = '{}/{}.topics'.format(os.path.dirname(__file__), robot)
        self.topics = TopicList(topics_file).topics
        parsed_args = Shortcuts(arg, self.topics, 'bag', __doc__, __version__)
        self.enabled = parsed_args.enabled
        self.name = parsed_args.name
        self.process = None
        self.bag()

    def bag(self):
        """Bag topics to folder."""
        topics = (' '.join(elem.topics) for elem in self.enabled)
        topics = ' '.join(topics)
        folder = self.name
        while not folder:
            folder = raw_input("name me: ")
        folder = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-') + folder

        if not os.path.exists(folder):
            os.makedirs(folder)

        cmd = split('rosbag record --split --duration=15 '
                    '{} -O {}/split'.format(topics, folder))

        self.process = Popen(cmd)

    def wait(self):
        """Wait for bag to terminate."""
        self.process.wait()

    def kill(self):
        """Kill bagging process."""
        self.process.kill()
        self.process.terminate()


if __name__ == '__main__':
    try:
        robot = os.environ["ROBOT"]
        bag = Bagger(sys.argv, robot)
        bag.wait()
    except KeyError:
        print "E: 'ROBOT' variable not exported properly."
        print "did you install the 'compsys' package correctly?"
        sys.exit(2)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            bag.kill()
        except NameError:
            sys.exit(1)
