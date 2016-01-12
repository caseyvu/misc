#!/usr/bin/env python
import re, sys

def derivative_molecules(m):
    results = []
    for k in TRANSLATION:
        V = TRANSLATION[k]
        n_matches = len(re.findall(k, m))
        for v in V:
            results.extend([re.sub('^((.*?%s){%d}.*?)%s' % (k, i, k), '\\1'+v, m) for i in xrange(n_matches)])
    return results

def reverse_engineer(m):
    steps = [m]
    while steps[-1] != 'e':
        next = re.sub('^(.*)(' + '|'.join(R_TRANSLATION.keys()) + ')(.*?)$',lambda x: x.group(1) + R_TRANSLATION[x.group(2)] + x.group(3),steps[-1])
        steps.append(next)
    return steps

with open(sys.argv[1]) as infile:
    data = [line.strip() for line in infile if len(line.strip()) > 0]

TRANSLATION = dict()
R_TRANSLATION = dict()
for d in data[:-1]:
    f, t = [v.strip() for v in d.split('=>')]
    if f in TRANSLATION:
        TRANSLATION[f].append(t)
    else:
        TRANSLATION[f] = [t]
    R_TRANSLATION[t] = f
MOLECULE= data[-1]

print "(a) Result: %d" % len(set(derivative_molecules(MOLECULE)))
print "(b) Result: %d" % (len(reverse_engineer(MOLECULE)) - 1)