#!/usr/bin/env python
import sys

TICKET = {"children": 3, "cats": 7, "samoyeds": 2,
          "pomeranians": 3, "akitas": 0, "vizslas": 0,
          "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

def check_data_against_tickets_day16a(data):
    for name in data:
        if name in TICKET:
            if TICKET[name] != data[name]:
                return False
    return True

def check_data_against_tickets_day16b(data):
    for name in data:
        if name in TICKET:
            if name == 'cats' or name == 'trees':
                if data[name] <= TICKET[name]:
                    return False
            elif name == 'pomeranians' or name == 'goldfish':
                if data[name] >= TICKET[name]:
                    return False
            else:
                if TICKET[name] != data[name]:
                    return False
    return True


RESULTS = list()
lineIndex = 0
SUE_DATA = list()
with open(sys.argv[1]) as infile:
    for line in infile:
        lineIndex += 1
        line = line.strip()
        tempIndex = line.find(':')
        line = line[tempIndex+2:]

        data = dict()
        details = line.split(', ')
        for detail in details:
            name, value = detail.split(': ')
            value = int(value)
            data[name] = value
        SUE_DATA.append(data)

# Part 1
index = 0
for data in SUE_DATA:
    index += 1
    if check_data_against_tickets_day16a(data):
        print "(a) Aunt Sue #%d" % index
        break

# Part 2
index = 0
for data in SUE_DATA:
    index += 1
    if check_data_against_tickets_day16b(data):
        print "(b) Aunt Sue #%d" % index
        break




