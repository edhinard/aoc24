#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    def recursivefindtrail(row, col, tails=None):
        if tails is None:
            tails = set()
        height = topographicmap[row][col]
        if height == MAX_HEIGHT:
            tails.add((row,col))
            return
        for dr,dc in ((-1,0), (0,-1), (0,+1), (+1,0)):
            if row+dr<0 or row+dr>=rowmax or col+dc<0 or col+dc>=colmax:
                continue
            if topographicmap[row+dr][col+dc] == height + 1:
                recursivefindtrail(row+dr, col+dc, tails)
        score = len(tails)
        return score
# solution: 789


if aoc.part == "two":
    def recursivefindtrail(row, col):
        rating = 0
        height = topographicmap[row][col]
        if height == MAX_HEIGHT:
            return 1
        for dr,dc in ((-1,0), (0,-1), (0,+1), (+1,0)):
            if row+dr<0 or row+dr>=rowmax or col+dc<0 or col+dc>=colmax:
                continue
            if topographicmap[row+dr][col+dc] == height + 1:
                rating += recursivefindtrail(row+dr, col+dc)
        return rating
# solution: 1735


topographicmap = [line for line in aoc.Input(split="", convert=int)]
rowmax = len(topographicmap)
colmax = len(topographicmap[0])
MAX_HEIGHT = 9

res = 0
for row in range(rowmax):
    for col in range(colmax):
        if topographicmap[row][col] == 0:
            res += recursivefindtrail(row, col)
print(res)
