#!/usr/bin/env python
import sys

def calculate(sizes):
    sizes.sort()
    area = sizes[0] * sizes[1] * 3 + 2*(sizes[0]*sizes[2] + sizes[1]*sizes[2])
    length = 2*(sizes[0] + sizes[1]) + reduce(lambda x, y: x*y, sizes)
    return (area, length)

results = list()
with open(sys.argv[1]) as infile:
    for line in infile:
        sizes = [int(s) for s in line.split('x')]
        results.append(calculate(sizes))
print "Wrap paper area: %d" % sum([a for a, _ in results])
print "Ribbon length: %d" % sum([l for _, l in results])
