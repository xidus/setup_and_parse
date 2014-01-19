#!/usr/bin/python -OB
# -*- coding: utf-8 -*-
# Version: Sat 4 May 2013
#   * Initial build.
#

"""
Module containing the auxiliary function setup_and_parse()
"""

import argparse


def setup_and_parse(desc, arglist):
    """
    Returns namespace with parsed arguments.

    Example:
    --------

    arglist = [
        (('hours'), dict(type=float, help='Number of hours')),
        (('-b', '--beg'), dict(type=int, default=26, help='First included week number')),
        (('-e', '--end'), dict(type=int, default=35, help='Last included week number')),
        (('-d', '--display'), dict(action='store_true', help='Display the months')),
    ]

    """

    # Initialise parser
    parser = argparse.ArgumentParser(description=desc)
    for flags, kwargs in arglist:
        if isinstance(flags, str) or isinstance(flags, unicode):
            parser.add_argument(flags, **kwargs)
        else:
            parser.add_argument(*flags, **kwargs)

    # Parse arguments
    return parser.parse_args()


