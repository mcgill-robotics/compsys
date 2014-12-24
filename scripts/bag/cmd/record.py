# -*- coding: utf-8 -*-

"""McGill Robotics' ROS Bag Recorder.

This tool records all the specified topics into 15 second bags to the
specified directory. Press Ctrl+C to stop.

By default, all topics defined in your team's 'topics' will be recorded if no
arguments are given. Otherwise, only the topics specified will be recorded.

The generated bags can be later merged using the `bag merge` command.
"""

__author__ = "Anass Al-Wohoush"
__version__ = "1.0"

import os
from shlex import split
from subprocess import Popen
from datetime import datetime


class Record(object):

    """Record topics into bags and splits them.

    Attributes:
        topics: List of topics to bag.
        name: Name of bag.
        dir: Path to record bags to.
        process: Bagging subprocess.
    """

    # Duration of each bag in seconds
    DURATION = 15

    def __init__(self, topics, name, dir):
        """Construct Record object.

        Args:
            topics: List of topics to bag.
            name: Name of bag.
            dir: Path to record bags to.
        """
        self.topics = topics
        self.name = name
        self.dir = dir
        self.process = None

    def run(self):
        """Bag topics to dir."""
        topics = (' '.join(elem.topics) for elem in self.topics)
        topics = ' '.join(topics)

        dir = self.name
        while not dir:
            dir = raw_input("name me: ")
        dir = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-") + dir
        dir = os.path.join(self.dir, dir)

        if not os.path.exists(dir):
            os.makedirs(dir)

        cmd = split("rosbag record --split --duration={} "
                    "{} -O {}/split".format(Record.DURATION, topics, dir))

        print("recording to {dir}".format(dir=dir))
        print("ctrl+c to stop")

        self.process = Popen(cmd)

        try:
            self.wait()
        except KeyboardInterrupt:
            pass
        finally:
            self.kill()

        return 0

    def wait(self):
        """Wait for bag to terminate."""
        self.process.wait()

    def kill(self):
        """Kill bagging process."""
        self.process.kill()
        self.process.terminate()
