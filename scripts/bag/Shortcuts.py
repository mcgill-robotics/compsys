"""Parse command line arguments for shortcuts."""

import argparse


class Shortcuts(object):

    """Parse command line arguments for shortcuts."""

    def __init__(self, arg, raw, executable, description, version):
        """Construct Shortcuts object.

        :param arg: command-line arguments
        :type arg: list of str
        :param raw: list of shortcuts to parse
        :type raw: TopicList
        :param executable: name of executable
        :type executable: str
        :param description: executable description for usage
        :type description: str
        :param version: version of the executable
        :type version: str
        """
        self.arg = arg[1:]
        self.raw = raw
        self.name = None
        self.executable = executable
        self.description = description
        self.version = version
        self.enabled = []
        self.parse()

    def parse(self):
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(
            prog=self.executable, add_help=False,
            description=self.description
        )

        # COMMON ARGUMENTS
        parser.add_argument(
            '--help', action='store_true',
            help='show this help message and exit'
        )
        parser.add_argument(
            '--version', action='version',
            version='%(prog)s {v}'.format(v=self.version)
        )
        parser.add_argument(
            '--name', nargs=1, help='output name'
        )

        # CUSTOM SHORTCUTS
        for elem in self.raw:
            parser.add_argument(
                '-' + elem.shortcut,
                const=elem, action='store_const',
                help=elem.description,
            )

        # PARSE
        args = vars(parser.parse_args())
        if args['help']:
            parser.print_help()
            exit()
        self.name = args['name'][0] if args['name'] else None
        self.enabled = [
            elem for elem in args.itervalues()
            if type(elem) not in (bool, str, list) and elem
        ]
        if not self.enabled:
            self.enabled = self.raw
