"""Parse command line arguments for shortcuts."""

import sys
import getopt


class Shortcuts(object):

    """Parse command line arguments for shortcuts."""

    def __init__(self, arg, raw):
        """Construct Shortcuts object."""
        self._file = arg[0][2:] if arg[0].startswith('./') else arg[0]
        self.arg = arg[1:]
        self.raw = raw
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
        """Print element information."""
        shortcut = elem.shortcut
        description = elem.description
        print '-{0: <9} {1: <69}'.format(shortcut, description)

    def usage(self):
        """Print usage based on configuration."""
        print 'usage: python {} [OPTIONS]'.format(self._file)
        print '{0: <10} {1: <69}'.format('OPTION', 'DESCRIPTION')
        for elem in self.raw:
            self._print_topic_info(elem)
