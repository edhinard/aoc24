#! /usr/bin/env python3

import aoc


def dijkstra(memory):
    memory[0][0] = 0
    queue = [(0, 0, 0)] # length, x, y
    while queue:
        queue.sort()
        length, x, y = queue.pop(0)
        if x == XMAX and y == YMAX:
            return length
        for dx, dy in ((+1,0), (0,+1), (-1,0), (0,-1)):
            if x+dx < 0 or x+dx > XMAX or y+dy < 0 or y+dy > YMAX:
                continue
            if memory[y+dy][x+dx] == "#":
                continue
            if memory[y+dy][x+dx] == ".":
                memory[y+dy][x+dx] = length + 1
            else:
                previouslength = memory[y+dy][x+dx]
                if previouslength <= length+1:
                    continue
            queue.append((length+1, x+dx, y+dy))
    return None

if aoc.test:
    XMAX = YMAX = 6
    COUNT = 12
else:
    XMAX = YMAX = 70
    COUNT = 1024


if aoc.part == "one":
    memory = [["." for _x in range(XMAX+1)] for _y in range(YMAX+1)]
    fallingbytes = aoc.Input(split=",", convert=int)
    for _ in range(COUNT):
        x,y = next(fallingbytes)
        memory[y][x] = "#"
    print(dijkstra(memory))


if aoc.part == "two":
    count = COUNT
    while True:
        memory = [["." for _x in range(XMAX+1)] for _y in range(YMAX+1)]
        fallingbytes = aoc.Input(split=",", convert=int)
        for _ in range(count):
            x,y = next(fallingbytes)
            memory[y][x] = "#"
        lastx, lasty = x,y
        if dijkstra(memory) is None:
            print(lastx,lasty)
            import sys
            sys.exit()
        count += 1
