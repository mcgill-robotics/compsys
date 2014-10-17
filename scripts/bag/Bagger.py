#!/usr/bin/env python

"""Topic bagging manager."""

import os
import sys
from datetime import datetime
from shlex import split
from Shortcuts import Shortcuts
from Topics import TopicList
from subprocess import *


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
        self.enabled = Shortcuts(arg, self.topics, 'bag').enabled
        self.process = None
        self.bag()

    def bag(self):
        """Bag topics to folder."""
        topics = (' '.join(elem.topics) for elem in self.enabled)
        topics = ' '.join(topics)
        folder = None
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
        print "E: 'ROBOT' variable not exported properly"
        sys.exit(2)
    except KeyboardInterrupt:
        bag.kill()
    except Exception as e:
        print e
        bag.kill()
