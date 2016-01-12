#!/usr/bin/env python
import sys, itertools

def product_of_list(l):
    return reduce(lambda x,y: x*y, l)

def find_min_quantum_entanglement(num_of_groups):
    GROUP_WEIGHT = WEIGHT_SUM / num_of_groups
    MIN_VALUE = None
    found = False
    for l in range(len(WEIGHTS)):
        for comb in itertools.combinations(WEIGHTS,l+1):
            if sum(comb) == GROUP_WEIGHT:
                found = True
                p = product_of_list(comb)
                if MIN_VALUE is None or p < MIN_VALUE:
                    MIN_VALUE = p
        if found:
            break
    return MIN_VALUE

with open(sys.argv[1]) as infile:
    WEIGHTS = [int(line.strip()) for line in infile]
WEIGHT_SUM = sum(WEIGHTS)

print "(a) Result: %d" % find_min_quantum_entanglement(3)
print "(b) Result: %d" % find_min_quantum_entanglement(4)