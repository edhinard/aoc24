#! /usr/bin/env python3

import re

import aoc


dirs = ((-1,0), (0,+1), (+1,0), (0,-1))
map = []
for r, row in enumerate(aoc.Input(split="")):
    map.append(row)
    try:
        c = row.index("^")
        gr, gc, gd = r, c, 0
        count = 1
        map[r][c] = "X"
    except:
        pass
rmax = len(map)
cmax = len(map[0])

if aoc.part == "one":
    while True:
        dr, dc = dirs[gd]
        newr = gr + dr
        newc = gc + dc
        if newr<0 or newr>=rmax or newc<0 or newc>=cmax:
            break
        match map[newr][newc]:
            case "#":
                gd = (gd + 1) % 4
            case ".":
                count += 1
                gr,gc = newr,newc
                map[gr][gc] = "X"
            case "X":
                gr,gc = newr,newc
    print(count)        
# solution: 


def isatimetrap(map, gr, gc, gd):
    dirs = ((-1,0), (0,+1), (+1,0), (0,-1))
    rmax = len(map)
    cmax = len(map[0])
    while True:
        dr, dc = dirs[gd]
        newr = gr + dr
        newc = gc + dc
        if newr<0 or newr>=rmax or newc<0 or newc>=cmax:
            return False
        match map[newr][newc]:
            case "#":
                gd = (gd + 1) % 4
            case ".":
                gr,gc = newr,newc
                map[gr][gc] = "1"
            case "1":
                gr,gc = newr,newc
                map[gr][gc] = "2"
            case "2":
                gr,gc = newr,newc
                map[gr][gc] = "3"
            case "3":
                gr,gc = newr,newc
                map[gr][gc] = "4"
            case "4":
                return True


if aoc.part == "two":
    res = 0
    for r in range(rmax):
        for c in range(cmax):
            map = list(aoc.Input(split=""))
            map[gr][gc] = "1"
            if map[r][c] == ".":
                map[r][c] = "#"
                if isatimetrap(map, gr, gc, gd):
                    #print()
                    #map[gr][gc] = "^"
                    #map[r][c] = "O"
                    #print("\n".join("".join(line) for line in map))
                    #print()
                    res += 1
    print(res)
# solution: !1530
