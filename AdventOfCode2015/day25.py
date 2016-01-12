#!/usr/bin/env python

START = 20151125
MUL = 252533
MODULO = 33554393

ROW, COL = (2947,3029)

def find_index(r, c):
    actual_row = r + c - 1
    prev_row = actual_row - 1
    index = ((prev_row+1)*prev_row)/2 + c
    return index

def find_value(index):
    index -= 1
    value = START
    for i in range(index):
        value = (value * MUL) % MODULO
    return value

print find_value(find_index(ROW,COL))
