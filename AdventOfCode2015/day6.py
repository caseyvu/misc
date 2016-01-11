#!/usr/bin/env python
import sys, re

pattern = re.compile("([a-z ]+) (\d+,\d+) through (\d+,\d+)")
def parse_instruction(s):
    m = pattern.match(s)
    if m is not None:
        command = m.group(1)
        x1, y1 = [int(v) for v in m.group(2).split(',')]
        x2, y2 = [int(v) for v in m.group(3).split(',')]
        return (command, (x1, y1), (x2, y2))
    return None

def turn_on_a(x_coords, y_coords):
    global GRIDS
    for x in range(x_coords[0], x_coords[1]+1):
        for y in range(y_coords[0], y_coords[1]+1):
            GRIDS[x][y] = 1

def turn_off_a(x_coords, y_coords):
    global GRIDS
    for x in range(x_coords[0], x_coords[1]+1):
        for y in range(y_coords[0], y_coords[1]+1):
            GRIDS[x][y] = 0

def toggle_a(x_coords, y_coords):
    global GRIDS
    for x in range(x_coords[0], x_coords[1]+1):
        for y in range(y_coords[0], y_coords[1]+1):
            if GRIDS[x][y] == 0:
                GRIDS[x][y] = 1
            else:
                GRIDS[x][y] = 0

def turn_on_b(x_coords, y_coords):
    global GRIDS
    for x in range(x_coords[0], x_coords[1]+1):
        for y in range(y_coords[0], y_coords[1]+1):
            GRIDS[x][y] += 1

def turn_off_b(x_coords, y_coords):
    global GRIDS
    for x in range(x_coords[0], x_coords[1]+1):
        for y in range(y_coords[0], y_coords[1]+1):
            if GRIDS[x][y] > 0:
                GRIDS[x][y] -= 1

def toggle_b(x_coords, y_coords):
    global GRIDS
    for x in range(x_coords[0], x_coords[1]+1):
        for y in range(y_coords[0], y_coords[1]+1):
            GRIDS[x][y] += 2

def count_light():
    global GRIDS
    return sum([sum(GRIDS[x]) for x in range(SIZE)])

def apply_instruction_day6a(command, coord1, coord2):
    x_coords = [coord1[0], coord2[0]]
    x_coords.sort()
    y_coords = [coord1[1], coord2[1]]
    y_coords.sort()
    if command == 'turn on':
        turn_on_a(x_coords, y_coords)
    elif command == 'turn off':
        turn_off_a(x_coords, y_coords)
    elif command == 'toggle':
        toggle_a(x_coords, y_coords)

def apply_instruction_day6b(command, coord1, coord2):
    x_coords = [coord1[0], coord2[0]]
    x_coords.sort()
    y_coords = [coord1[1], coord2[1]]
    y_coords.sort()
    if command == 'turn on':
        turn_on_b(x_coords, y_coords)
    elif command == 'turn off':
        turn_off_b(x_coords, y_coords)
    elif command == 'toggle':
        toggle_b(x_coords, y_coords)

instructions = list()
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        instruction = parse_instruction(line)
        if instruction is not None:
            instructions.append(instruction)

# Part 1
SIZE = 1000
GRIDS = [[0 for i in range(SIZE)] for j in range(SIZE)]
for command, coord1, coord2 in instructions:
    apply_instruction_day6a(command, coord1, coord2)
print "Light Count (a): %d" % count_light()

# Part 2
GRIDS = [[0 for i in range(SIZE)] for j in range(SIZE)]
for command, coord1, coord2 in instructions:
    apply_instruction_day6b(command, coord1, coord2)
print "Light Count (b): %d" % count_light()