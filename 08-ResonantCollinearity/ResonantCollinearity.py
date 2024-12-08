#! /usr/bin/env python3

import itertools

import aoc

antennasbyfrequency = {}
rowmax = 0
colmax = 0
for row, line in enumerate(aoc.Input(split="")):
    rowmax = max(rowmax, row)
    for col, location in enumerate(line):
        colmax = max(colmax, col)
        if location != ".":
            antennasbyfrequency.setdefault(location, []).append((row, col))


if aoc.part == "one":
    antinodes = set()
    for antennas in antennasbyfrequency.values():
        for (ra,ca),(rb,cb) in itertools.combinations(antennas, 2):
            r = 2*rb - ra
            c = 2*cb - ca
            if r >= 0 and r <= rowmax and c >= 0 and c <= colmax:
                antinodes.add((r,c))
            r = 2*ra - rb
            c = 2*ca - cb
            if r >= 0 and r <= rowmax and c >= 0 and c <= colmax:
                antinodes.add((r,c))
    print(len(antinodes))
# solution: 261


if aoc.part == "two":
    antinodes = set()
    for antennas in antennasbyfrequency.values():
        for (ra,ca),(rb,cb) in itertools.combinations(antennas, 2):
            for r in range(rowmax+1):
                for c in range(colmax+1):
                    if (c-ca)*(r-rb) - (c-cb)*(r-ra) == 0:
                        antinodes.add((r,c))
    print(len(antinodes))
# solution: 898
