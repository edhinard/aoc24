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
        warehousemap.append(expandedline)
    height = len(warehousemap)
    width = len(warehousemap[0])

    def canmove(move, row, col):
        moves = {
            "<": (0,-1),
            "^": (-1,0),
            ">": (0,+1),
            "v": (+1,0),
        }
        dr,dc = moves[move]
        newrow = row + dr
        newcol = col + dc
        match warehousemap[row][col]:
            case "@":
                return canmove(move, newrow, newcol)
            case "#":
                return False
            case ".":
                return True
            case "[":
                can = canmove(move, newrow, newcol)
                if can and move in "^v":
                    warehousemap[row][col] = "."
                    can &= canmove(move, row, col+1)
                    warehousemap[row][col] = "["
                return can
            case "]":
                can = canmove(move, newrow, newcol)
                if can and move in "^v":
                    warehousemap[row][col] = "."
                    can &= canmove(move, row, col-1)
                    warehousemap[row][col] = "]"
                return can

    def domove(move, row, col):
        moves = {
            "<": (0,-1),
            "^": (-1,0),
            ">": (0,+1),
            "v": (+1,0),
        }
        dr,dc = moves[move]
        newrow = row + dr
        newcol = col + dc
        item = warehousemap[row][col]
        warehousemap[row][col] = "."
        match item:
            case "@":
                domove(move, newrow, newcol)
            case "#":
                raise AssertionError(f"cannot move {move} wall at {row=} {col=}")
            case ".":
                return row, col
            case "[":
                domove(move, newrow, newcol)
                if move in "^v":
                    domove(move, row, col+1)
            case "]":
                domove(move, newrow, newcol)
                if move in "^v":
                    domove(move, row, col-1)
        warehousemap[newrow][newcol] = item
        return newrow, newcol


    for move in itertools.chain.from_iterable(next(paragraphs)):
        if canmove(move, robotrow, robotcol):
            robotrow, robotcol = domove(move, robotrow, robotcol)

    gps = 0
    for row in range(height):
        for col in range(width):
            if warehousemap[row][col] == "[":
                gps += row * 100 + col
    print(gps)
