#! /usr/bin/env python3

import aoc

MIN = 1
MAX = 3
def safe(report):
    delta = report[1] - report[0]
    previous = report[0]
    for level in report[1:]:
        if abs(level-previous) > MAX or abs(level-previous) < MIN:
            break
        if (level-previous) * delta < 0:
            break
        previous = level
    else:
        return True
    return False


if aoc.part == "one":
    print(sum(safe(report) for report in aoc.Input(convert=int, split=" ")))
# solution: 321


if aoc.part == "two":
    count = 0
    for report in aoc.Input(convert=int, split=" "):
        if safe(report):
            count += 1
            continue
        for i in range(len(report)):
            r = report[:]
            del r[i]
            if safe(r):
                count += 1
                break
    print(count)
# solution: 386
