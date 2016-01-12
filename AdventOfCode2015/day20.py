#!/usr/bin/env python
from math import sqrt, floor

TARGET = 29000000

def sum_of_divisible_a(number):
    total = 0
    root_square = sqrt(number)
    for i in range(1, int(floor(root_square))+1):
        if number % i == 0:
            d = number / i
            total += d + i
    return total * 10

def sum_of_divisible_b(number):
    total = 0
    root_square = sqrt(number)
    for i in range(1, int(floor(root_square))+1):
        if number % i == 0:
            d = number / i
            if d <= 50:
                total += i
            if i <= 50:
                total += d
    return total * 11

# Part 1
for n in range(1, 800000):
    sum_value = sum_of_divisible_a(n)
    if sum_value >= TARGET:
        print "(a) Result: %d" % n
        break

# Part 2
for n in range(1, 800000):
    sum_value = sum_of_divisible_b(n)
    if sum_value >= TARGET:
        print "(b) Result: %d" % n
        break


