#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IELTS Writing Essay Creator
# License: Apache

__version__ = 'v0.1.0.3 Alpha'
__author__ = 'Will Skywalker'

from sys import argv
import single_chart
  

def main():
    print 'IETLS Writing Essay Creator', __version__, '\n'
    if len(argv) == 1 :
        single_chart.main()

if __name__ == '__main__':
    main()
