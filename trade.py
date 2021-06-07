#!/usr/bin/env python3

import sys
import os

from utils import usage, error_handling

from src import main_logic

def main() -> int:
    usage.usage()
    try:
        obj = main_logic.Trade()
        if obj.start() == 84:
            return 84
    except Exception as e:
        print(f'Error when logging in: {e}')
        return 84
    return 0


if __name__ == '__main__':
    exit(main())
