#!/usr/bin/env python
START = 'hepxcrrq'

print "This is just partial solution.\nA complete solution should include cases where the \"HEAD\" of the old password",
print "can (already) satisfy some of the conditions.\nHere we assume the conditions can only be satisfied with all the last 5 characters."

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_VALID = [c for c in ALPHABET if c not in 'ilo']

def increase_by_one(original):
    if len(original) < 1:
        return ALPHABET_VALID[0]
    c= original[-1]
    c_index = ALPHABET_VALID.index(c)
    if c_index >= len(ALPHABET_VALID) - 1:
        return increase_by_one(original[:-1]) + ALPHABET_VALID[0]
    return original[:-1] + ALPHABET_VALID[c_index+1]

VALID_TAILS = list()
for i in range(len(ALPHABET)-2):
    inscreasing_seq = ALPHABET[i:i+3]
    invalid = False
    for c in 'ilo':
        if c in inscreasing_seq:
            invalid = True
            break
    if invalid:
        continue
    inscreasing_seq = inscreasing_seq[0] + inscreasing_seq + inscreasing_seq[2]
    VALID_TAILS.append(inscreasing_seq)

collections = list()
l = len(START)
for tail in VALID_TAILS:
    result = START[:l-5] + tail
    if result < START:
        result = increase_by_one(START[:l-5]) + tail
    collections.append(result)
collections.sort()
print "Part 1: %s" % collections[0]
print "Part 2: %s" % collections[1]