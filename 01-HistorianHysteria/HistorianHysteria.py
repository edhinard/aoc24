#! /usr/bin/env python3

import aoc

a, b = list(zip(*aoc.Input(convert=int, split="  "), strict=True))

if aoc.part == "one":
    print(sum(abs(x-y) for x,y in zip(sorted(a), sorted(b), strict=True)))
# solution: 2815556

if aoc.part == "two":
    print(sum(x * b.count(x) for x in a))
# solution: 23927637
