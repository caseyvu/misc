#!/usr/bin/env python
import sys, json

def recursive_sum_in_list(data, exclude_red=False):
    total = 0
    for e in data:
        if isinstance(e, int):
            total += e
        elif isinstance(e, list):
            total += recursive_sum_in_list(e, exclude_red=exclude_red)
        elif isinstance(e, dict):
            total += recursive_sum_in_dict(e, exclude_red=exclude_red)
    return total

def recursive_sum_in_dict(data, exclude_red=False):
    total = 0
    if exclude_red:
        has_red = False
        for k in data:
            v = data[k]
            if v == 'red':
                has_red = True
                break
        if has_red:
            return total

    for k in data:
        e = data[k]
        if isinstance(e, int):
            total += e
        elif isinstance(e, list):
            total += recursive_sum_in_list(e, exclude_red=exclude_red)
        elif isinstance(e, dict):
            total += recursive_sum_in_dict(e, exclude_red=exclude_red)
    return total

def recursive_sum(data, exclude_red=False):
    if isinstance(data, list):
         return recursive_sum_in_list(data, exclude_red=exclude_red)
    elif isinstance(data, dict):
         return recursive_sum_in_dict(data, exclude_red=exclude_red)

with open(sys.argv[1]) as infile:
    data = json.load(infile)

print "Total: %d" % recursive_sum(data)
print "Total (exclude red): %d" % recursive_sum(data, exclude_red=True)



