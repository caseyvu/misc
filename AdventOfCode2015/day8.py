#!/usr/bin/env python
import sys

def decode_length_diff(s):
    org_len = len(s)
    processed = s[1:-1].decode('string_escape')
    return org_len - len(processed)

SPECIALS = set(["\\","\""])
def encode_length_diff(s):
    return sum([1 if c in SPECIALS else 0 for c in s]) + 2

lines = list()
with open(sys.argv[1]) as infile:
    lines = [line.strip() for line in infile]

# Part 1
print "Length Difference (a): %d" % sum([decode_length_diff(line) for line in lines])
# Part 2
print "Length Difference (b): %d" % sum([encode_length_diff(line) for line in lines])