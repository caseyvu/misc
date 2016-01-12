#!/usr/bin/env python
import sys

SIZE = 100

def spoilt_bulbs(board):
    for i in [0, SIZE-1]:
        for j in [0, SIZE-1]:
            board[i][j] = 1

def new_board(spoilt=False):
    temp = [[0 for i in range(SIZE)] for j in range(SIZE)]
    if spoilt:
        spoilt_bulbs(temp)
    return temp

def count_light(board):
    return sum([sum(row) for row in board])

def number_of_on_neighbors(board, j, i):
    cnt = 0
    minJ = j - 1 if j > 1 else 0
    maxJ = j + 1 if j < SIZE-1 else SIZE-1
    minI = i - 1 if i > 1 else 0
    maxI = i + 1 if i < SIZE-1 else SIZE-1
    for jj in range(minJ,maxJ+1):
        for ii in range(minI, maxI+1):
            if ii != i or jj != j:
               cnt += board[jj][ii]
    return cnt

def next_board(board, spoilt=False):
    result = new_board(spoilt)
    for j in range(SIZE):
        for i in range(SIZE):
            cur_state = board[j][i]
            neighbors = number_of_on_neighbors(board, j, i)
            if cur_state == 1:
                if (neighbors == 2 or neighbors == 3):
                    result[j][i] = 1
            else:
                if neighbors == 3:
                    result[j][i] = 1
    return result


INITIAL_BOARD = new_board()
with open(sys.argv[1]) as infile:
    j = 0
    for line in infile:
        line = line.strip()
        i = 0
        for c in line:
            if c == '#':
                INITIAL_BOARD[j][i] = 1
            i += 1
        j += 1

# Part 1
curr_board = INITIAL_BOARD
for a in range(100):
    curr_board = next_board(curr_board)
print "(a) Result: %d" % count_light(curr_board)

# Part 2
curr_board = INITIAL_BOARD
spoilt_bulbs(curr_board)
for a in range(100):
    curr_board = next_board(curr_board, spoilt=True)
print "(b) Result: %d" % count_light(curr_board)