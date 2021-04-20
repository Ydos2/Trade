import sys


def check_period(i):
    try:
        int(i)
    except Exception:
        print("Input Error: All arguments must be positive integers", file=sys.stderr)
        sys.exit(84)
