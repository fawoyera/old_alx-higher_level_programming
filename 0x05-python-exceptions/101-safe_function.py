#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as ex:
        sys.stderr.write("Exception: " + str(ex) + '\n')
        return None
