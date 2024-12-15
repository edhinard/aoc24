#! /usr/bin/env python3

import itertools

import aoc

if aoc.part == "one":
    paragraphs = aoc.Input(split="", groupby="paragraph")
    warehousemap = []
    for row,line in enumerate(next(paragraphs)):
        if "@" in line:
            robotrow = row
            robotcol = line.index("@")
            line[robotcol] = "."
        warehousemap.append(line)
    height = len(warehousemap)
    width = len(warehousemap[0])

    moves = {
        "<": (0,-1),
        "^": (-1,0),
        ">": (0,+1),
        "v": (+1,0),
    }
    for move in itertools.chain.from_iterable(next(paragraphs)):
        dr,dc = moves[move]
        newrobotrow = robotrow + dr
        newrobotcol = robotcol + dc
        if warehousemap[newrobotrow][newrobotcol] == "#":
            continue
        if warehousemap[newrobotrow][newrobotcol] == ".":
            robotrow = newrobotrow
            robotcol = newrobotcol
            continue
        row = newrobotrow
        col = newrobotcol
        while warehousemap[row][col] == "O":
            row += dr
            col += dc
        if warehousemap[row][col] == "#":
            continue
        robotrow = newrobotrow
        robotcol = newrobotcol
        warehousemap[robotrow][robotcol] = "."
        warehousemap[row][col] = "O"

    gps = 0
    for row in range(height):
        for col in range(width):
            if warehousemap[row][col] == "O":
                gps += row * 100 + col
    print(gps)


if aoc.part == "two":
    paragraphs = aoc.Input(split="", groupby="paragraph")
    warehousemap = []
    for row,line in enumerate(next(paragraphs)):
        expand = {
            "#": "##",
            "O": "[]",
            ".": "..",
            "@": "@.",
        }
        expandedline = list("".join(expand[item] for item in line))
        if "@" in expandedline:
            robotrow = row
            robotcol = expandedline.index("@")
            #expandedline[robotcol] = "."
        warehousemap.append(expandedline)
    height = len(warehousemap)
    width = len(warehousemap[0])

    def recursivemove(move, row=None, col=None):
        global robotrow, robotcol
        robot = row is None and col is None
        if robot:
            row, col = robotrow, robotcol
        moves = {
            "<": (0,-1),
            "^": (-1,0),
            ">": (0,+1),
            "v": (+1,0),
        }
        dr,dc = moves[move]
        newrow = row + dr
        newcol = col + dc
        match item := warehousemap[row][col]:
            case "@":
                canmove = recursivemove(move, newrow, newcol)
            case "#":
                return False
            case ".":
                return True
            case "[":
                canmove = recursivemove(move, newrow, newcol)
                if canmove and move in "^v":
                    warehousemap[row][col] = "."
                    canmove &= recursivemove(move, row, col+1)
                    warehousemap[row][col] = "["
            case "]":
                canmove = recursivemove(move, newrow, newcol)
                if canmove and move in "^v":
                    warehousemap[row][col] = "."
                    canmove &= recursivemove(move, row, col-1)
                    warehousemap[row][col] = "]"
        if canmove:
            warehousemap[row][col] = "."
            warehousemap[newrow][newcol] = item
            if robot:
                robotrow, robotcol = newrow, newcol
        return canmove


    for move in itertools.chain.from_iterable(next(paragraphs)):
        recursivemove(move)
    #for line in warehousemap:
    #    print("".join(line))

    gps = 0
    for row in range(height):
        for col in range(width):
            if warehousemap[row][col] == "[":
                gps += row * 100 + col
    print(gps)

#1545461 too high
