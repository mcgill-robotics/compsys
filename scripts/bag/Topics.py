"""Topics manager."""

import sys
import ConfigParser


class Topic(object):

    """Create topic object from configuration."""

    def __init__(self, name, config):
        """Construct Topic object."""
        self.name = name
        self.description = config.get(name, 'description')
        self.shortcut = config.get(name, 'shortcut')
        self.topics = config.get(name, 'topics').split('\n')


class TopicList(object):

    """Create topics object from configuration file."""

    def __init__(self, filename):
        """Construct TopicList object."""
        self._config = ConfigParser.ConfigParser()
        self._config.read(filename)
        self.filename = filename
        self.topics = []
        self.parse()

    def parse(self):
        """Parse topics from configuration file."""
        try:
            self.topics = [
                Topic(topic, self._config)
                for topic in self._config.sections()
            ]
            if not self.topics:
                err = "'{}' either missing or empty".format(self.filename)
                raise ValueError(err)
        except (ConfigParser.NoOptionError, ValueError) as exception:
            print 'E:', exception
            sys.exit(2)


if __name__ == '__main__':
    topic_list = TopicList('auv.topics')
    for topic in topic_list.topics:
        print topic.name, topic.shortcut
