#!/usr/bin/env python
import sys

def next_coordinate(cur_coord, instruction):
    if instruction == '>':
        return (cur_coord[0]+1,cur_coord[1])
    if instruction == '<':
        return (cur_coord[0]-1,cur_coord[1])
    if instruction == '^':
        return (cur_coord[0],cur_coord[1]+1)
    if instruction == 'v':
        return (cur_coord[0],cur_coord[1]-1)
    return None

def locations_set_with_steps(steps):
    cur_coord = (0,0)
    locations = [cur_coord]
    for instruction in steps:
        cur_coord = next_coordinate(cur_coord, instruction)
        if cur_coord is not None:
            locations.append(cur_coord)
    return set(locations)

def day3a(steps):
    locations = locations_set_with_steps(steps)
    return len(locations)

def day3b(steps):
    santaSteps = steps[::2]
    roboSteps = steps[1::2]
    locations1 = locations_set_with_steps(santaSteps)
    locations2 = locations_set_with_steps(roboSteps)
    locations = locations1.union(locations2)
    return len(locations)

with open(sys.argv[1]) as infile:
    steps = infile.read().strip()

print "Location Count (Santa only): %d" % day3a(steps)
print "Location Count (Santa+Robot): %d" % day3b(steps)
