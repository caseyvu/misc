#!/usr/bin/env python
import sys, re, itertools

pattern = re.compile("(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).")
def parse_line(line):
    m = pattern.match(line)
    if m is not None:
        person1 = m.group(1)
        person2 = m.group(4)
        v = int(m.group(3))
        if m.group(2) == 'lose':
            v = -v
        return (person1, person2, v)
    return None

def score(seats):
    global SCORE_MAP
    l = len(seats)
    scores = list()
    for i in range(l):
        me = seats[i]
        if i == 0:
            left = seats[-1]
        else:
            left = seats[i-1]
        if i == l - 1:
            right = seats[0]
        else:
            right = seats[i+1]
        scores.append(SCORE_MAP[(me,left)])
        scores.append(SCORE_MAP[(me,right)])
    return sum(scores)


PERSONS = set()
SCORE_MAP = dict()
with open(sys.argv[1]) as infile:
    for line in infile:
        person1, person2, v = parse_line(line.strip())
        SCORE_MAP[(person1, person2)] = v
        PERSONS.add(person1)
        PERSONS.add(person2)

# Part 1
PERSON_LIST = list(PERSONS)
MAX_SCORE = None
for p in itertools.permutations(PERSON_LIST):
    s = score(p)
    if MAX_SCORE is None or s > MAX_SCORE:
        MAX_SCORE = s
print "Max score (a): %d" % MAX_SCORE

# Part 2
myself = "myself"
for person in PERSONS:
    SCORE_MAP[(myself,person)] = 0
    SCORE_MAP[(person, myself)] = 0
PERSONS.add("myself")
PERSON_LIST = list(PERSONS)
MAX_SCORE = None
for p in itertools.permutations(PERSON_LIST):
    s = score(p)
    if MAX_SCORE is None or s > MAX_SCORE:
        MAX_SCORE = s
print "Max score (b): %d" % MAX_SCORE



