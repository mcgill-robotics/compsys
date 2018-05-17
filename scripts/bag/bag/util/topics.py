# -*- coding: utf-8 -*-
"""Topics manager."""

import ConfigParser


class Topic(object):

    """Create Topic object from configuration.

    Attributes:
        name: Name of topic.
        description: Description of topic.
        shortcut: Shortcut to enable topic.
        topics: List of associated topics.
    """

    def __init__(self, name, config):
        """Construct Topic object.

        Args:
            name: Name of topic.
            config: ConfigParser containing topic.
        """
        self.name = name
        self.description = config.get(name, "description")
        self.shortcut = config.get(name, "shortcut")
        self.topics = config.get(name, "topics").split('\n')


class TopicList(object):

    """Create TopicList object from configuration file.

    Attributes:
        filename: Path to .topics file.
        topics: List of Topics parsed from 'topics' file.
    """

    def __init__(self, path):
        """Construct TopicList object.

        Args:
            path: Path to topics configuration file.
        """
        self.filename = path
        self.topics = []

        self._config = ConfigParser.ConfigParser()
        self._config.read(self.filename)
        self.parse()

    def parse(self):
        """Parse topics from configuration file.

        Raises:
            ConfigParser.NoOptionError: Missing option in 'topics' file.
            ValueError: Missing topics file.
        """
        self.topics = [
            Topic(topic, self._config) for topic in self._config.sections()
        ]
        if not self.topics:
            err = "'{}' either missing or empty".format(self.filename)
            raise ValueError(err)
