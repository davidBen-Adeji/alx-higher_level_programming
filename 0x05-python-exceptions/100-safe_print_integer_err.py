#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except NameError as name:
        print("Exception: {}".format(name), file=sys.stderr)
        return False
    except ValueError as value:
        print("Exception: {}".format(value), file=sys.stderr)
        return False
    except TypeError as typ:
        print("Exception: {}".format(typ), file=sys.stderr)
        return False
