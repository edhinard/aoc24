#! /usr/bin/env python3

import re

import aoc

if aoc.part == "one":
    res = 0
    for line in aoc.Input():
        for x,y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
            res += int(x)*int(y)
    print(res)
# solution: 190604937


if aoc.part == "two":
    res = 0
    do = True
    for line in aoc.Input():
        for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", line):
            if m.group(3):
                do = True
            elif m.group(4):
                do = False
            elif do:
                x = m.group(1)
                y = m.group(2)
                res += int(x)*int(y)
    print(res)
# solution: 82857512
