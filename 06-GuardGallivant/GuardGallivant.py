#! /usr/bin/env python3

import contextlib

import aoc

# read the map room
directions = ((-1,0), (0,+1), (+1,0), (0,-1))
room = []
for r, row in enumerate(aoc.Input(split="")):
    room.append(row)
    with contextlib.suppress(ValueError):
        c = row.index("^")
        initialguardrow, initialguardcol, initialguarddir = r, c, 0
        count = 1
        room[r][c] = "X"


# find solution for part #1
guardrow, guardcol, guarddir = initialguardrow, initialguardcol, initialguarddir
height = len(room)
width = len(room[0])
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


if aoc.part == "one":
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
    guardrow, guardcol, guarddir = initialguardrow, initialguardcol, initialguarddir
    for r in range(height):
        for c in range(width):
            # reuse part #1 map room where all visited places are marked with an X
            # set an obstacle on each visited places to see if it creates a loop
            if (r,c) != (guardrow,guardcol) and room[r][c] == "X":
                roomcopy = list(aoc.Input(split=""))
                roomcopy[guardrow][guardcol] = "1"
                roomcopy[r][c] = "#"
                if isatimetrap(roomcopy, guardrow, guardcol, guarddir):
                    count += 1
    print(count)
# solution: 1530
