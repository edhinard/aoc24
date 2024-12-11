#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    stones = [*next(aoc.Input(split=" "))]
    for _ in range(25):
        newstones = []
        for stone in stones:
            if stone == "0":
                newstones.append("1")
            elif len(stone) % 2 == 0:
                half = len(stone)//2
                if half > 1:
                    alldigit = False
                a = stone[:half]
                newstones.append(a)
                b = stone[half:].lstrip("0") or "0"
                newstones.append(b)
            else:
                newstones.append(str(int(stone) * 2024))
        stones = newstones
    print(len(stones))

if aoc.part == "two":
    stones = [*next(aoc.Input(split=" "))]
    def blink75(stones):
        for _ in range(75):
            print(_, len(stones))
            newstones = []
            for stone in stones:
                if stone == "0":
                    newstones.append("1")
                elif len(stone) % 2 == 0:
                    half = len(stone)//2
                    if half > 1:
                        alldigit = False
                    a = stone[:half]
                    newstones.append(a)
                    b = stone[half:].lstrip("0") or "0"
                    newstones.append(b)
                else:
                    newstones.append(str(int(stone) * 2024))
            stones = [s for s in newstones if len(s)>1]
            if not stones:
                break
    for stone in stones:
        print()
        blink75([stone])