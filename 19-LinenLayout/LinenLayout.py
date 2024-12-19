#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    input = aoc.Input().read().splitlines()
    patterns = {}
    for p in input.pop(0).split(", "):
        patterns.setdefault(p[0], []).append(p)
    input.pop(0)
    
    impossibles = set()

    def possible(towel):
        if not towel:
            return True
        if towel in impossibles:
            return False
        p = towel[0]
        for pattern in patterns.get(p, []):
            if towel.startswith(pattern) and possible(towel[len(pattern):]):
                return True
        impossibles.add(towel)
        return False

    count = 0
    for i, towel in enumerate(input):
        if possible(towel):
            count += 1
    print(count)


if aoc.part == "two":
    pass