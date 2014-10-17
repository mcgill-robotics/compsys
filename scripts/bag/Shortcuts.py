"""Parse command line arguments for shortcuts."""

import sys
import getopt


class Shortcuts(object):

    """Parse command line arguments for shortcuts."""

    def __init__(self, arg, raw, executable):
        """Construct Shortcuts object.

        :param arg: command-line arguments
        :type arg: list of str
        :param raw: list of shortcuts to parse
        :type raw: TopicList
        :param executable: name of executable
        :type executable: str
        """
        self.arg = arg[1:]
        self.raw = raw
        self.executable = executable
        self.enabled = []
        self.parse()

    def parse(self):
        """Parse command line arguments."""
        shortcuts = ''.join(elem.shortcut for elem in self.raw)
        try:
            opts, args = getopt.getopt(self.arg, shortcuts, ["help"])
        except getopt.GetoptError:
            print 'E: Invalid option'
            self.usage()
            sys.exit(1)

        for opt, arg in opts:
            if opt == "--help":
                self.usage()
                sys.exit()
            else:
                for elem in self.raw:
                    if opt == '-' + elem.shortcut:
                        self.enabled.append(elem)
                        break

        if not self.enabled:
            self.enabled = self.raw

    def _print_topic_info(self, elem):
        """Print element information.

        :param elem: object with shortcut and description
        :type elem: Topic
        """
        shortcut = elem.shortcut
        description = elem.description
        print '-{0: <9} {1: <69}'.format(shortcut, description)

    def usage(self):
        """Print usage based on configuration."""
        print 'usage: python {} [OPTIONS]'.format(self.executable)
        print '{0: <10} {1: <69}'.format('OPTION', 'DESCRIPTION')
        for elem in self.raw:
            self._print_topic_info(elem)
