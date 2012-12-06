#!usr/bin/env python
# -*- coding: utf-8 -*-

#Author J. R. Carroll
#Date Started:  10/22/2012

import datetime
import sys

def main(*args):
    if args == ([],):
        print "jPyTime requires a START time, and a number of hours you will work"
    else:
        start_time = args[1]
    pass
    
    

if __name__ == "__main__":
    main(sys.argv[1:])


