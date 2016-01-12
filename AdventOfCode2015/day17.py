#!/usr/bin/env python
import sys, itertools

def possible_way(min_number_container=False):
    count = 0
    found = False
    for r in range(len(CONTAINERS)):
        for comb in itertools.combinations(CONTAINERS, r+1):
            volumns = sum(comb)
            if volumns == REQ_VOLUME:
                found = True
                count += 1
        if min_number_container and found:
            break
    return count

CONTAINERS = []
REQ_VOLUME = 150
with open(sys.argv[1]) as infile:
    for line in infile:
        CONTAINERS.append(int(line.strip()))
CONTAINERS.sort()

print "(a) Result: %d" % possible_way(min_number_container=False)
print "(b) Result: %d" % possible_way(min_number_container=True)