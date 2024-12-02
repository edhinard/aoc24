#! /usr/bin/env python3

import itertools

import aoc

MIN = 1
MAX = 3
def safe(report):
    trend = report[-1] - report[0]
    for deltalevel in (level-previous for previous,level in itertools.pairwise(report)):
        if abs(deltalevel) > MAX or abs(deltalevel) < MIN:
            return False
        if deltalevel * trend <= 0:
            return False
    return True


if aoc.part == "one":
    print(sum(safe(report) for report in aoc.Input(convert=int, split=" ")))
# solution: 321

def relaxedsafe(report):
    if safe(report):
        return True
    for i in range(len(report)):
        r = report[:]
        del r[i]
        if safe(r):
            return True
    return False

if aoc.part == "two":
    print(sum(relaxedsafe(report) for report in aoc.Input(convert=int, split=" ")))
# solution: 386
