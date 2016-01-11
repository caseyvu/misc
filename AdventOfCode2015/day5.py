#!/usr/bin/env python
import sys

VOWELS = 'aeiou'
TABOOS = ['ab', 'cd', 'pq', 'xy']
def found_double(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def has_repeated_pair(s):
    pair_index = dict()
    for i in range(len(s)-1):
        pair = s[i:i+2]
        if pair in pair_index:
            pair_index[pair].append(i)
        else:
            pair_index[pair] = [i]
    for pair in pair_index:
        indices = pair_index[pair]
        if len(indices) >= 2:
            indices.sort()
            if indices[-1] - indices[0] >= 2:
                return True
    return False

def has_repeated_letter_with_one_in_between(s):
    string_even = s[::2]
    string_odd = s[1::2]
    return found_double(string_even) or found_double(string_odd)

def check_string_day5a(s):
    # Condition 3
    for t in TABOOS:
        if t in s:
            return False
    # Condition 2
    if found_double(s) is False:
        return False
    # Condition 1
    vowels_count = 0
    for c in s:
        if c in VOWELS:
            vowels_count += 1
    return vowels_count >= 3

def day5a(lines):
    counter = 0
    for line in lines:
        if check_string_day5a(line):
            counter += 1
    return counter

def day5b(lines):
    counter = 0
    for line in lines:
        if has_repeated_letter_with_one_in_between(line) and has_repeated_pair(line):
            counter += 1
    return counter

lines = list()
with open(sys.argv[1]) as infile:
    lines = [line.strip() for line in infile]

print "Nice string count (5a): %d" % day5a(lines)
print "Nice string count (5b): %d" % day5b(lines)
