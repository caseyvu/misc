#!/usr/bin/env python
import sys

def parse_line(line):
    parts = [p.strip(',+') for p in line.split()]
    if parts[0] == 'jmp':
        parts[1] = int(parts[1])
    elif parts[0] == 'jie' or parts[0] == 'jio':
        parts[2] = int(parts[2])
    return parts

def execute():
    line_index = 0
    while line_index < len(INSTRUCTIONS):
        inst = INSTRUCTIONS[line_index]
        cmd = inst[0]
        if cmd == 'tpl':
            REGISTERS[inst[1]] *= 3
        elif cmd == 'hlf':
            REGISTERS[inst[1]] /= 2
        elif cmd == 'inc':
            REGISTERS[inst[1]] += 1

        if cmd in ['jmp','jie','jio']:
            if cmd == 'jmp':
                line_index += inst[1]
            elif cmd == 'jie':
                v = REGISTERS[inst[1]]
                if v % 2 == 0:
                    line_index += inst[2]
                else:
                    line_index += 1
            elif cmd == 'jio':
                v = REGISTERS[inst[1]]
                if v == 1:
                    line_index += inst[2]
                else:
                    line_index += 1
        else:
            line_index += 1

INSTRUCTIONS = list()
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        INSTRUCTIONS.append(parse_line(line))

# Part 1
REGISTERS = {'a':0,'b':0}
execute()
print '(a) b=%d' % REGISTERS['b']

# Part 2
REGISTERS = {'a':1,'b':0}
execute()
print '(b) b=%d' % REGISTERS['b']

