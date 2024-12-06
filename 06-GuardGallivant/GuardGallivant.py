#! /usr/bin/env python3

import contextlib

import aoc

directions = ((-1,0), (0,+1), (+1,0), (0,-1))
room = []
for r, row in enumerate(aoc.Input(split="")):
    room.append(row)
    with contextlib.suppress(ValueError):
        c = row.index("^")
        guardrow, guardcol, guarddir = r, c, 0
        count = 1
        room[r][c] = "X"
height = len(room)
width = len(room[0])

if aoc.part == "one":
    while True:
        deltarow, deltacol = directions[guarddir]
        newr = guardrow + deltarow
        newc = guardcol + deltacol
        if newr<0 or newr>=height or newc<0 or newc>=width:
            break
        match room[newr][newc]:
            case "#":
                guarddir = (guarddir + 1) % 4
            case ".":
                count += 1
                guardrow,guardcol = newr,newc
                room[guardrow][guardcol] = "X"
            case "X":
                guardrow,guardcol = newr,newc
    print(count)
# solution: 4663


def isatimetrap(room, guardrow, guardcol, guarddir):
    directions = ((-1,0), (0,+1), (+1,0), (0,-1))
    height = len(room)
    width = len(room[0])
    while True:
        deltarow, deltacol = directions[guarddir]
        newr = guardrow + deltarow
        newc = guardcol + deltacol
        if newr<0 or newr>=height or newc<0 or newc>=width:
            return False
        match room[newr][newc]:
            case "#":
                guarddir = (guarddir + 1) % 4
            case ".":
                guardrow,guardcol = newr,newc
                room[guardrow][guardcol] = "1"
            case "1":
                guardrow,guardcol = newr,newc
                room[guardrow][guardcol] = "2"
            case "2":
                guardrow,guardcol = newr,newc
                room[guardrow][guardcol] = "3"
            case "3":
                guardrow,guardcol = newr,newc
                room[guardrow][guardcol] = "4"
            case "4":
                return True


if aoc.part == "two":
    count = 0
    for r in range(height):
        for c in range(width):
            room = list(aoc.Input(split=""))
            room[guardrow][guardcol] = "1"
            if room[r][c] == ".":
                room[r][c] = "#"
                if isatimetrap(room, guardrow, guardcol, guarddir):
                    count += 1
    print(count)
# solution: 1530
