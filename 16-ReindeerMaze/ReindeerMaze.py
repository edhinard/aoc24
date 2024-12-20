#! /usr/bin/env python3

import functools

import aoc


def findbestpaths(maze, startrow, startcol, endrow, endcol):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3
    directions = {EAST: (0,+1), SOUTH:(+1,0), WEST:(0,-1), NORTH:(-1, 0)}

    # The nodes of the graph
    #  keys are (row, col, direction) -- position in the maze
    #  values are (score, tiles) -- score and visited tiles up to that position
    nodes = {(startrow, startcol, EAST): (0, {(startrow, startcol)})}

    # The working queue is a set of positions initialized with: start position, eastwards
    queue = {(startrow, startcol, EAST)}

    # A Dijkstra algorithm to find minimum score for each nodes
    while queue:
        #  Poping out the lowest score position from queue
        score, position = min((nodes[pos][0], pos) for pos in queue)
        queue.remove(position)
        row, col, direction = position
        score, tiles = nodes[position]

        # Evaluate the three next nodes from here (new position, new score, new visited tiles, nextposition):
        #  forward: one tile forward increase the score of 1
        #  right and left: stay on the same tile but change direction and increase the score of 1000
        dr, dc = directions[direction]
        forward = ((row + dr, col + dc, direction), score + 1, tiles | {(row + dr, col + dc)}, row + dr, col + dc)
        rightdirection = (direction + 1) % len(directions)
        dr, dc = directions[rightdirection]
        right = ((row, col, rightdirection), score + 1000, set(tiles), row + dr, col + dc)
        leftdirection = (direction - 1) % len(directions)
        dr, dc = directions[leftdirection]
        left  = ((row, col, leftdirection), score + 1000, set(tiles), row + dr, col + dc)

        # Loop on those 3 possible next nodes
        #  * filter out nodes that:
        #    - are not in the graph (walls)
        #    - are already visited with a better score
        #  * update queue and nodes
        for position, score, tiles, nextrow, nextcol in (forward, right, left):
            row, col, direction = position
            if maze[row][col] == "#" or maze[nextrow][nextcol] == "#":
                continue
            if position in nodes:
                previousscore, previoustiles = nodes[position]
                if previousscore < score:
                    continue
                if previousscore == score:
                    tiles |= previoustiles  # noqa: PLW2901
            nodes[position] = (score, tiles)
            queue.add(position)

    # Collect the best paths at position E
    endnodes = [nodes[(endrow, endcol, direction)] for direction in range(4) if (endrow, endcol, direction) in nodes]
    endnodes.sort()
    bestscore = endnodes[0][0]
    besttiles = (tiles for score, tiles in endnodes if score == bestscore)
    return bestscore, functools.reduce(set.union, besttiles)


maze = []
for row,line in enumerate(aoc.Input(split="")):
    if "S" in line:
        startrow = row
        startcol = line.index("S")
        line[startcol] = "."
    if "E" in line:
        endrow = row
        endcol = line.index("E")
        line[endcol] = "."
    maze.append(line)

bestscore, besttiles = findbestpaths(maze, startrow, startcol, endrow, endcol)


if aoc.part == "one":
    print(bestscore)
if aoc.part == "two":
    print(len(besttiles))
