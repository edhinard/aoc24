#! /usr/bin/env python3

import aoc

left, right = zip(*aoc.Input(convert=int, split=None), strict=True)

if aoc.part == "one":
    print(sum(abs(x-y) for x,y in zip(sorted(left), sorted(right), strict=True)))
# solution: 2815556

if aoc.part == "two":
    print(sum(x * right.count(x) for x in left))
# solution: 23927637
