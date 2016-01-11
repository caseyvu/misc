#!/usr/bin/env python
START = '3113322113'

def put_into_groups(text):
    cur = None
    cur_cnt = 0
    groups = []
    for c in text:
        if cur is None:
            cur = c
            cur_cnt += 1
        elif cur != c:
            groups.append((cur, cur_cnt))
            cur = c
            cur_cnt = 1
        else:
            cur_cnt += 1
    groups.append((cur, cur_cnt))
    return groups

def form_new_number(groups):
    result = ''
    for c, count in groups:
        result += str(count) + c
    return result

# Part 1
text = START
for i in range(40):
    groups = put_into_groups(text)
    text = form_new_number(groups)
print "Result (a): %d" % len(text)

# Part 2
for i in range(10):
    groups = put_into_groups(text)
    text = form_new_number(groups)
print "Result (b): %d" % len(text)