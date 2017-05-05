#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit
from apple.disk import *


def show_catalog(diskfile):
    if not diskfile:
        print('Cannot execute without a disk filename !!!')
        exit()

    dsk = DiskDos33(diskfile)
    dsk.catalog()

if __name__ == "__main__":
    file = "".join(argv[1:])
    show_catalog(file)
