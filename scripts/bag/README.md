# McGill Robotics ROS Bagger

This tool is designed to simplify the ROS bagging process.
For now, it can:

* Record the specified topics into 15 second bags to a specified directory.

* Merge previously recorded bags from a specified directory.

By default, all the topics defined in your project's `topics` file will be
recorded/merged if no arguments are specified. Otherwise, only the topics
specified will be recorded/merged.

## Usage
If the `compsys` package is installed correctly, the tool should already be
mapped to `bag` in your terminal.

To begin, you can run:

```bash
bag --help
```

## How is this better than `rosbag`?

### Issues with `rosbag`
This tool was designed when the builtin `rosbag` tool was determined to be not
up to McGill Robotics standards.

* An unexpected failure such as a sudden crash (e.g. overheating) or loss of
  power (e.g. from a kill switch) would cause the corruption of all bagged data
  from the current run.

* Managing all the bags was unmaintainable. A few hours of testing would
  yield several gigabytes of arbitrarily named bags that were very cumbersome
  to filter through.

* One person usually only needs but a few topics or a few seconds from a bag,
  but would have to copy and play the whole run through it manually later on.

### Our improvements
The above issues were addressed as follows:

* The bags are split every 15 seconds. This means we can only lose up to 15
  seconds of data were an unexpected failure to happen.

* The user is forced to name the bag and each run is separated by folder.

* The user can merge specific topics from the recorded bags and can select
  only a few of the bags to merge.

Moreover, `bag` was not only designed to help automate and manage the recording
of ROS topics, but to accelerate development and testing significantly as well.
This includes the following improvements:

* One rarely bags a single topic, so `bag` supports topic groups that can be
  defined in a `topics` file (See [FAQs](3-how-do-i-configure-my-topics)).

* Writing out long topics is cumbersome, so `bag` has customizable shortcuts
  that map to them for you.

## FAQs

### 1. I need more help
Usage information and help can be found by simply running

```bash
bag --help
```

from anywhere in the terminal.

For help regarding recording or merging, simply run:

```bash
bag record --help
bag merge --help
```

respectively.

### 2. I am an expert and want to know more
Expertly run:
```bash
bag --help
```

### 3. How do I configure my topics?
This tool determines the topics to look from a `topics` file located in your
project's root repository (i.e. `$ROBOTIC_PATH/$ROBOT/topics`).

The `topics` file is formatted like an `ini` file. It consists of a list of
topic groups defined as such:

```ini
[UNIQUE GROUP NAME]
shortcut: UNIQUE ONE CHARACTER SHORTCUT FOR CLI
description: SHORT DESCRIPTION OF TOPICS FOR --help
topics: TOPIC/NUMBER/ONE
        TOPIC/NUMBER/TWO
```

where the `UNIQUE GROUP NAME` should be human readable, the `shortcut` should
be a unique character to be used as a command line argument, the `description`
should be a brief phrase describing what this group of topics holds and the
`topics` should be a list of the associated topic names recognized by ROS. *The
list of topics should be separated by new lines and aligned properly using
spaces.*

A sample `topics` file would look like:

```ini
[battery]
shortcut: b
description: battery voltages
topics: electrical_interface/batteryVoltage1
        electrical_interface/batteryVoltage2

[motor]
shortcut: m
description: sent motor commands
topics: electrical_interface/motor

[state estimation]
shortcut: s
description: IMU pose and TFs
topics: state_estimation/pose
        state_estimation/raw
        tf

[temperature]
shortcut: t
description: CPU temperatures
topics: status/temperature
```

## Version History
**1.1** (June 15, 2015)
* Add `--split` argument.
**1.0** (December 24, 2014)
* Initial release.
