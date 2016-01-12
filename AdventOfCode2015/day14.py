#!/usr/bin/env python
import sys, re

pattern = re.compile("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
def parse_line(line):
    m = pattern.match(line)
    if m is not None:
        return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
    return None

def distance(speed, time_fly, time_rest, total_time):
    time_round = time_fly + time_rest
    rounds = total_time / time_round
    extra_time_fly = total_time % time_round
    if extra_time_fly > time_fly:
        extra_time_fly = time_fly
    return rounds * speed * time_fly + speed * extra_time_fly

REINDEERS = list()
REINDEERS_SCORE = dict()
TOTAL_TIME = 2503
with open(sys.argv[1]) as infile:
    for line in infile:
        data = parse_line(line.strip())
        REINDEERS.append(data)
        REINDEERS_SCORE[data[0]] = 0

# Part 1
distances = [distance(r[1], r[2], r[3], TOTAL_TIME) for r in REINDEERS]
print "(a) Max distance: %d" % max(distances)

# Part 2
for s in range(TOTAL_TIME):
    MAX_DIST = None
    distances = dict()
    for r in REINDEERS:
        d = distance(r[1], r[2], r[3], s+1)
        if d in distances:
            distances[d].append(r[0])
        else:
            distances[d] = [r[0]]
        if MAX_DIST is None or d > MAX_DIST:
            MAX_DIST = d

    for name in distances[MAX_DIST]:
        REINDEERS_SCORE[name] += 1

print "(b) Max point: %d" % max([REINDEERS_SCORE[r] for r in REINDEERS_SCORE])
