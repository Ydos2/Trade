import sys
import os


def usage():
    print("SYNOPSIS\n"
          "    ./groundhog period\n\n"
          "DESCRIPTION\n"
          "    period        the number of days defining a period")


def check_args(args: list) -> int:
    if "-h" in args or "--help" in args:
        usage()
        exit(0)
    if len(sys.argv) != 2:
        usage()
        return 84
