#!/usr/bin/env python
import sys, re, itertools

pattern = re.compile("([a-z]+) to ([a-z]+) = (\d+)")
def parse_line(s):
    m = pattern.match(s)
    if m is not None:
        distance = int(m.group(3))
        return (m.group(1), m.group(2), distance)
    return None

CITIES = set()
DISTANCES = dict()
def add_data(city1, city2, distance):
    global CITIES, DISTANCES
    CITIES.add(city1)
    CITIES.add(city2)
    DISTANCES[(city1, city2)] = distance
    DISTANCES[(city2, city1)] = distance

def cost_for_path(p):
    cost = 0
    curr_pos = p[0]
    for next_pos in p[1:]:
        cost += DISTANCES[(curr_pos, next_pos)]
        curr_pos = next_pos
    return cost

with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip().lower()
        data = parse_line(line)
        if data is not None:
            city1, city2, distance = data
            add_data(city1, city2, distance)

cities_list = list(CITIES)
costs_collections = list()
for p in itertools.permutations(cities_list):
    costs_collections.append(cost_for_path(p))

print "Shortest: %d" % min(costs_collections)
print "Longest: %d" % max(costs_collections)

