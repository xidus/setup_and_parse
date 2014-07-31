#!/usr/bin/python -OB
# -*- coding: utf-8 -*-
# Version: Sun 9 Feb 2014
#   * Added conversion function for type=dt.date
#
# Version: Sat 4 May 2013
#   * Initial build.
#

"""
Auxiliary functions for easy setup and parsing with Python's argparse module.

Main work horse is the the function `setup_and_parse()`


"""

import argparse


def sap_date(string):
    import datetime as dt
    fmt = '%Y-%m-%d'
    try:
        value = dt.datetime.strptime(string, fmt).date()
    except:
        msg = '{} does not conform to ISO format (\'{}\')'.format(string, fmt)
        raise argparse.ArgumentTypeError(msg)
    return value


def sap_datetime(string):

    import datetime as dt

    fmts = [
        '%Y-%m-%d',
        '%Y-%m-%dT%H:%M',
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%dT%H:%M:%S.%f',
    ]

    value = None
    for fmt in fmts:
        try:
            value = dt.datetime.strptime(string, fmt)
        except:
            continue

    if value is None:
        msg = '{} does not conform to ISO formats (\'{}\')'.format(
            string, ', '.join(fmts)
        )
        raise argparse.ArgumentTypeError(msg)

    return value


def setup_and_parse(desc, arglist):
    """
    Returns namespace with parsed arguments.

    Example
    -------
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


