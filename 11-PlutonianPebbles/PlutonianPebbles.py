#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    numblinks = 25


if aoc.part == "two":
    numblinks = 75


stones = {s:1 for s in next(aoc.Input(split=" "))}
for _ in range(numblinks):
    newstones = {}
    for stone, count in stones.items():
        if stone == "0":
            newstones.setdefault("1", 0)
            newstones["1"] += count
        elif len(stone) % 2 == 0:
            half = len(stone)//2
            if half > 1:
                alldigit = False
            a = stone[:half]
            newstones.setdefault(a, 0)
            newstones[a] += count
            b = stone[half:].lstrip("0") or "0"
            newstones.setdefault(b, 0)
            newstones[b] += count
        else:
            s = str(int(stone) * 2024)
            newstones.setdefault(s, 0)
            newstones[s] += count
    stones = newstones
print(sum(stones.values()))
