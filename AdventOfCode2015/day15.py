#!/usr/bin/env python
import sys

def score(splits, calories_requirement=None):
    if calories_requirement is not None:
        calories = 0
        for values, number in zip(INGREDIENTS,splits):
            calories += number * values[4]
        if calories != calories_requirement:
            return None

    aspects = [0,0,0,0]
    for values, number in zip(INGREDIENTS,splits):
        for i in range(len(aspects)):
            aspects[i] += number * values[i]
    return reduce(lambda x, y: x*y, [v if v >= 0 else 0 for v in aspects])

INGREDIENTS = list()
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        tempIndex = line.find(':')
        line = line[tempIndex+2:]

        details = line.split(', ')
        values = list()
        for detail in details:
            _, value = detail.split(' ')
            value = int(value)
            values.append(value)

        INGREDIENTS.append(values)

# Part 1
MAX_AMOUNT = 100
MAX_SCORE = None
for a in range(MAX_AMOUNT + 1):
    for b in range(MAX_AMOUNT + 1 - a):
        for c in range(MAX_AMOUNT + 1 - a - b):
            d = MAX_AMOUNT - a - b - c
            s = score([a,b,c,d])
            if MAX_SCORE is None or MAX_SCORE < s:
                MAX_SCORE = s
print "(a) Max score: %d" % MAX_SCORE

# Part 2
MAX_SCORE = None
for a in range(MAX_AMOUNT + 1):
    for b in range(MAX_AMOUNT + 1 - a):
        for c in range(MAX_AMOUNT + 1 - a - b):
            d = MAX_AMOUNT - a - b - c
            s = score([a,b,c,d],calories_requirement=500)
            if MAX_SCORE is None or MAX_SCORE < s:
                MAX_SCORE = s
print "(b) Max score: %d" % MAX_SCORE



