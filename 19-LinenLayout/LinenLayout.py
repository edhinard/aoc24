#! /usr/bin/env python3

import aoc

lines = aoc.Input().read().splitlines()
patterns = {}
for p in lines.pop(0).split(", "):
    patterns.setdefault(p[0], []).append(p)
lines.pop(0)
towels = list(lines)

counts = {}
def possible(towel, count=0):
    if not towel:
        return 1
    if towel in counts:
        return counts[towel]
    counts[towel] = 0
    p = towel[0]
    for pattern in patterns.get(p, []):
        if towel.startswith(pattern):
            counts[towel] += possible(towel[len(pattern):], count)
    return counts[towel]


if aoc.part == "one":
    print(sum(1 for towel in towels if possible(towel)))


if aoc.part == "two":
    print(sum(possible(towel) for towel in towels))
