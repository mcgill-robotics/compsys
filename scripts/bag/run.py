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

import os
import sys
from util import Parser, TopicList

__author__ = "Anass Al-Wohoush"
__version__ = "1.2.0"


if __name__ == "__main__":
    try:
        topics_path = os.environ["TOPICS_PATH"]
    except KeyError:
        print("E: TOPICS_PATH environment variable not set")
        sys.exit(2)

    topics = TopicList(topics_path)

    args = Parser(topics, __doc__, __version__)
    status = args.cmd(
        topics=args.enabled, name=args.name,
        dir=args.dir, args=args.raw
    ).run()

    sys.exit(status)
