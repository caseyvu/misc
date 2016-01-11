#!/usr/bin/env python
import sys, re

pattern = re.compile("(([a-z0-9]+) )?((LSHIFT|RSHIFT|OR|AND|NOT) )?([a-z0-9]+) -> ([a-z0-9]+)")
def parse_line(s):
    m = pattern.match(s)
    if m is not None:
        s1 = m.group(2)
        if s1 is not None:
            try:
                s1 = int(s1)
            except ValueError:
                pass
        s2 = m.group(5)
        if s2 is not None:
            try:
                s2 = int(s2)
            except ValueError:
                pass
        return (s1, m.group(4), s2, m.group(6))
    return None

def perform(op, v1, v2):
    if op == 'AND':
        return v1 & v2
    if op == 'OR':
        return v1 | v2
    if op == 'RSHIFT':
        return v1>>v2
    if op == 'LSHIFT':
        return v1<<v2
    if op == 'NOT':
        return ~v2
    if op is None:
       return v2

def add_instruction(instruction):
    global DB
    s1, op, s2, v = instruction
    instruction = (s1, op, s2)
    varCnt = 0
    for s in [s1, s2]:
        if s is not None and isinstance(s, int) is False:
            varCnt += 1
            if s in AFFECT:
                AFFECT[s].append(v)
            else:
                AFFECT[s] = [v]
    DB[v] = {'variable_sources':varCnt, 'instruction':instruction}

def process():
    global DB, PROCESSED
    while len(DB) > 0:
        wires = DB.keys()
        for w in wires:
            variable_sources = DB[w].get('variable_sources')
            if variable_sources == 0:
                s1, op, s2 = DB[w].get('instruction')
                v1 = None
                if isinstance(s1, int):
                    v1 = s1
                elif s1 is not None:
                    v1 = PROCESSED[s1]
                v2 = None
                if isinstance(s2, int):
                    v2 = s2
                elif s2 is not None:
                    v2 = PROCESSED[s2]
                value = perform(op, v1, v2)
                PROCESSED[w] = value
                DB.pop(w)

                affected = AFFECT.get(w)
                if affected is not None:
                    for a in affected:
                        DB[a]['variable_sources'] -= 1

RAW_INSTRUCTIONS = list()
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        instruction = parse_line(line)
        if instruction is not None:
            RAW_INSTRUCTIONS.append(instruction)

# Part 1
DB = dict()
PROCESSED = dict()
AFFECT = dict()
for instruction in RAW_INSTRUCTIONS:
    add_instruction(instruction)
process()
print "Day7a: a=%d" % PROCESSED['a']

# Part 2
old_a_value = PROCESSED['a']
DB = dict()
PROCESSED = dict()
AFFECT = dict()
for instruction in RAW_INSTRUCTIONS:
    if instruction[3] == 'b':
        instruction = (None, None,old_a_value,'b')
    add_instruction(instruction)
process()
print "Day7b: a=%d" % PROCESSED['a']


