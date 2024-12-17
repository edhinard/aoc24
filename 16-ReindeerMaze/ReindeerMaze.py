#! /usr/bin/env python3

import sys

import aoc



if aoc.part == "one":
    maze = []
    for row,line in enumerate(aoc.Input(split="")):
        if "S" in line:
            srow = row
            scol = line.index("S")
            line[scol] = "."
        maze.append(line)

    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3
    directions = [(0,+1), (+1,0), (0,-1), (-1, 0)]

    def extractmin(queue):
        score = sys.maxsize
        position = None
        for k, v in queue.items():
            if v < score:
                score = v
                position = k
        score = queue.pop(position)
        row, col, direction = position
        return score, row, col, direction

    pastpositions = set()
    def addinqueue(queue, score, row, col ,direction):
        global pastpositions
        position = (row, col, direction)
        if position in pastpositions:
            return
        pastpositions.add(position)
        position = (row, col ,direction)
        previousscore = queue.get(position, sys.maxsize)
        queue[position] = min(score, previousscore)

    queue = {(srow, scol, EAST): 0}
    bestscore = sys.maxsize
    while queue:
        score, row, col, direction = extractmin(queue)

        dr, dc = directions[direction]
        forward = (score + 1, row + dr, col + dc, direction, row + dr, col + dc)

        rightdirection = (direction + 1) % len(directions)
        dr, dc = directions[rightdirection]
        right = (score + 1000, row, col, rightdirection, row + dr, col + dc)

        leftdirection = (direction - 1) % len(directions)
        dr, dc = directions[leftdirection]
        left  = (score + 1000, row, col, leftdirection, row + dr, col + dc)

        for score, row, col, direction, nextrow, nextcol in (forward, right, left):
            if (place:=maze[row][col]) != "#" and maze[nextrow][nextcol] != "#":
                addinqueue(queue, score, row, col, direction)
            if place == "E":
                bestscore = min(bestscore, score)
    print(bestscore)


if aoc.part == "two":
    maze = []
    for row,line in enumerate(aoc.Input(split="")):
        if "S" in line:
            srow = row
            scol = line.index("S")
            line[scol] = "."
        maze.append(line)

    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3
    directions = [(0,+1), (+1,0), (0,-1), (-1, 0)]

    def extractmin(queue):
        score = sys.maxsize
        position = None
        for k, v in queue.items():
            if v[0] < score:
                score = v[0]
                position = k
        score, tiles = queue.pop(position)
        row, col, direction = position
        return score, tiles, row, col, direction

    pastpositions = {}
    bestscore = sys.maxsize
    besttiles = set()
    def addinqueue(queue, score, tiles, row, col ,direction):  # noqa: PLR0913
        global pastpositions, bestscore, besttiles
        position = (row, col, direction)
        s = pastpositions.get(position, sys.maxsize)
        if s < score:
            return
        pastpositions[position] = score
        position = (row, col ,direction)
        previousscore, previoustiles = queue.get(position, (sys.maxsize, set()))
        if previousscore < score:
            return
        if previousscore == score:
            tiles = tiles | previoustiles
        queue[position] = (score, tiles)
        if maze[row][col] == "E":
            if bestscore < score :
                return
            if bestscore == score:
                tiles = tiles | besttiles
            bestscore, besttiles = score, tiles


    bs = sys.maxsize
    queue = {(srow, scol, EAST): (0, {(srow,scol)})}
    while queue:
        score, tiles, row, col, direction = extractmin(queue)

        dr, dc = directions[direction]
        forward = (score + 1, tiles | {(row + dr, col + dc)}, row + dr, col + dc, direction, row + dr, col + dc)

        rightdirection = (direction + 1) % len(directions)
        dr, dc = directions[rightdirection]
        right = (score + 1000, set(tiles), row, col, rightdirection, row + dr, col + dc)

        leftdirection = (direction - 1) % len(directions)
        dr, dc = directions[leftdirection]
        left  = (score + 1000, set(tiles), row, col, leftdirection, row + dr, col + dc)

        for score, tiles, row, col, direction, nextrow, nextcol in (forward, right, left):
            if maze[row][col] != "#" and maze[nextrow][nextcol] != "#":
                addinqueue(queue, score, tiles, row, col, direction)
            if maze[row][col] == "E":
                bs = min(bs, score)

            #if maze[row][col] == "E":
            #    print(score, bestscore)
    print(bestscore, bs, len(besttiles))

    #for r,c in besttiles:
    #    maze[r][c] = "O"
    #for line in maze:
    #    print("".join(line))


# 433 too low