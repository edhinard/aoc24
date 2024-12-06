#! /usr/bin/env python3

import re

import aoc

if aoc.part == "one":
    res = 0

    hlines = list(aoc.Input())
    lr = sum(len(re.findall("XMAS", line)) for line in hlines)
    rl = sum(len(re.findall("SAMX", line)) for line in hlines)
    #rl = sum(len(re.findall("XMAS", "".join(reversed(line)))) for line in hlines)

    vlines = ["".join(vline) for vline in zip(*hlines)]
    td = sum(len(re.findall("XMAS", line)) for line in vlines)
    bu = sum(len(re.findall("SAMX", line)) for line in vlines)
    #bu = sum(len(re.findall("XMAS", "".join(reversed(line)))) for line in vlines)

    map = list(aoc.Input(split=""))
    n = len(map)
    diagmap = [["" for _ in range(2*n-1)] for _ in range(2*n-1)]
    for r in range(n):
        for c in range(n):
            x = n-1 + c - r
            y = r + c
            diagmap[x][y] = map[r][c]

    lines = ["".join(l) for l in diagmap]
    #print(lines)
    a = sum(len(re.findall("XMAS", line)) for line in lines)
    b = sum(len(re.findall("SAMX", line)) for line in lines)

    diagmap = [["" for _ in range(2*n-1)] for _ in range(2*n-1)]
    for r in range(n):
        for c in range(n):
            y = n-1 + c - r
            x = r + c
            diagmap[x][y] = map[r][c]

    lines = ["".join(l) for l in diagmap]
    #print(lines)
    c = sum(len(re.findall("XMAS", line)) for line in lines)
    d = sum(len(re.findall("SAMX", line)) for line in lines)



    print(lr,rl,td,bu,a,b,c,d)
    print(sum([lr,rl,td,bu,a,b,c,d]))
# solution: !2367


if aoc.part == "two":
    map = list(aoc.Input())
    n = len(map)
    res = 0
    for r in range(1,n-1):
        for c in range(1,n-1):
            if map[r][c] == "A":
                a = map[r-1][c-1] + map[r-1][c+1] + map[r+1][c+1] + map[r+1][c-1]
                if a in ["MMSS", "SMMS", "SSMM", "MSSM"]:
                    #print(r,c, a)
                    res += 1
    print(res)
# solution: 82857512
