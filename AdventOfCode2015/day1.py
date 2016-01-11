#!/usr/bin/env python
import sys

floor = 0
reached_basement = None
i = 0
with open(sys.argv[1]) as infile:
    instruction = infile.read()
    for c in instruction:
        i += 1
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if reached_basement is None and floor == -1:
            reached_basement = i
print "Final floor: %d" % floor
print "First basement: %d" % reached_basement




