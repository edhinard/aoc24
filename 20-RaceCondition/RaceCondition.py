#! /usr/bin/env python3

import aoc

racemap = []
for row, line in enumerate(aoc.Input(split="")):
    if "S" in line:
        startcol = line.index("S")
        startrow = row
    if "E" in line:
        endcol = line.index("E")
        endrow = row
    racemap.append(line)


# Walk the map the Dijkstra way to find the best times for all positions (= distance to start)
#  returns the dict of visited positions with their times
def besttimes(racemap, startposition):
    visited = {startposition: 0}
    queue = [(0, startposition)] # time, row, col
    while queue:
        queue.sort()
        time, (row, col) = queue.pop(0)
        for dr, dc in ((+1,0), (0,+1), (-1,0), (0,-1)):
            if racemap[row+dr][col+dc] != "#" and (row+dr, col+dc) not in visited:
                queue.append((time+1, (row+dr, col+dc)))
                visited[(row+dr, col+dc)] = time+1
    return visited


# Group the map position by their time (=distance) to the start position
#  compute the reference time from start to end
fromstart = {}
for position, time in besttimes(racemap, (startrow, startcol)).items():
    if position == (endrow, endcol):
        reftime = time
    fromstart.setdefault(time, []).append(position)

# Group the map position by their time (=distance) to the end position
fromend = {}
for position, time in besttimes(racemap, (endrow, endcol)).items():
    fromend.setdefault(time, []).append(position)


# Find all A and B in map where:
#  - there is a path from Start to A
#  - there is a path from B to End
#  - timeAB <= CHEATMAX
#  - timeSA + timeAB + timeBE <= reftime - SAVINGMIN
#
# S.............A.#..##..#..#...#...#B.............E
#  <-----------> <------------------> <----------->
#      timeSA           timeAB            timeBE

if aoc.part == "one":
    CHEATMAX = 2
    SAVINGMIN = 1 if aoc.test else 100
if aoc.part == "two":
    CHEATMAX = 20
    SAVINGMIN = 50 if aoc.test else 100

count = 0
savings = {}
for timeSA in range(reftime+1):
    for positionA in fromstart[timeSA]:
        for timeBE in range(reftime - SAVINGMIN - timeSA):
            for positionB in fromend[timeBE]:
                timeAB = abs(positionB[0] - positionA[0]) + abs(positionB[1] - positionA[1])
                if timeAB > CHEATMAX:
                    continue
                saving = reftime - (timeSA + timeAB + timeBE)
                if  saving >= SAVINGMIN:
                    savings.setdefault(saving, 0)
                    savings[saving] += 1
                    count += 1


for k,v in sorted(savings.items()):
    print(f" - There are {v} cheats that save {k} picoseconds.")
print(count)
