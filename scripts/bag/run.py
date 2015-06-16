#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""McGill Robotics ROS Bagger.

This tool can:

    1.  Record the specified topics into 15 second bags to the specified
        directory.

    2.  Merge previously recorded bags from the specified directory.

By default, all the topics defined in your project's 'topics' file will be
recorded/merged if no arguments are specified. Otherwise, only the topics
specified will be recorded/merged.
"""

import sys
from util import Parser, TopicList

__author__ = "Anass Al-Wohoush"
__version__ = "1.1"


if __name__ == "__main__":
    try:
        topics = TopicList().topics
    except KeyError:
        print("E: ROBOTIC_PATH and/or ROBOT environment variables not set.")
        print("did you install the 'compsys' package correctly?")
        sys.exit(2)

    args = Parser(topics, __doc__, __version__)
    status = args.cmd(
        topics=args.enabled, name=args.name,
        dir=args.dir, args=args.raw
    ).run()

    sys.exit(status)
