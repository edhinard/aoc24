#! /usr/bin/env python3

import copy

import aoc

if aoc.part == "one":
    def dijkstra(racemap):
        queue = [(0, startrow, startcol)] # time, row, col
        while queue:
            queue.sort()
            time, row, col = queue.pop(0)
            if row == endrow and col == endcol:
                return time
            for dr, dc in ((+1,0), (0,+1), (-1,0), (0,-1)):
                if racemap[row+dr][col+dc] == ".":
                    queue.append((time+1, row+dr, col+dc))
                    racemap[row+dr][col+dc] = time+1
        return None

    refracemap = []
    for row, line in enumerate(aoc.Input(split="")):
        if "S" in line:
            startcol = line.index("S")
            startrow = row
            line[startcol] = "."
        if "E" in line:
            endcol = line.index("E")
            endrow = row
            line[endcol] = "."
        refracemap.append(line)
    racemap = copy.deepcopy(refracemap)
    reftime = dijkstra(racemap)

    MAXSAVING = 100
    count = 0
    for row in range(1, len(refracemap)-1):
        for col in range(1, len(refracemap[0])-1):
            if refracemap[row][col] == "#":
                racemap = copy.deepcopy(refracemap)
                racemap[row][col] = "."
                saving = reftime - dijkstra(racemap)
                if saving >= MAXSAVING:
                    count += 1
    print(count)

if aoc.part == "two":
    pass

