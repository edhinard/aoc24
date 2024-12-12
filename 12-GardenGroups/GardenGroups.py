#! /usr/bin/env python3

import aoc

garden = list(aoc.Input(split=""))
rowmax = len(garden)
colmax = len(garden[0])

UP    = (-1, 0)
DOWN  = (+1, 0)
RIGHT = (0, +1)
LEFT  = (0, -1)

def neighbors(row, col):
    # returns the list of directions among UP, DOWN, LEFT, RIGHT where the
    # plant at (row, col) is connected to a similar plant (same letter, upper or lower)
    neigh = []
    plant = garden[row][col].upper()
    for direction in (UP, DOWN, LEFT, RIGHT):
        dr, dc = direction
        if row+dr>=0 and row+dr<rowmax and col+dc>=0 and col+dc<colmax and garden[row+dr][col+dc].upper() == plant:
            neigh.append(direction)
    return neigh

def recursiveregion(row, col, region=None):
    # recursive Depth First Search of a region of similar plants starting at (row, col)
    # returns a list of (row, col, neighbors)
    if region is None:
        region = []
    plant = garden[row][col]
    if not plant.isupper():
        return region
    neigh = neighbors(row, col)
    region.append((row, col, neigh))
    garden[row][col] = plant.lower()
    for dr, dc in neigh:
        r = row + dr
        c = col + dc
        recursiveregion(r, c, region)
    return region


if aoc.part == "one":
    def perimeter(region):
        # Each plant in the region has 4 sides, but only the sides behind which
        # there is another type of plant should be counted in the perimeter.
        return len(region) * 4 - sum(len(neigh) for _,_,neigh in region)


if aoc.part == "two":
    def perimeter(region):
        # In that part the perimeter is the number of sides of the polygonal region (including internal ones)
        # The count is carried out by type of sides: Top sides i.e. side of plants that have no neighbors above them...

        sides = 0

        # Top borders
        # keep plants in the region that do not have a neighbor above, sort them by row and then by column
        borderplants = sorted(((row, col) for row,col,neighbors in region if UP not in neighbors))
        previousr, previousc = -1, -1
        while borderplants:
            r,c = borderplants.pop(0)
            if r != previousr or c != previousc + 1:
                # series of contiguous plant on the same row count for only one side of the region
                sides += 1
            previousr, previousc = r, c

        # Bottom borders
        borderplants = sorted(((row, col) for row,col,neighbors in region if DOWN not in neighbors))
        previousr, previousc = -1, -1
        while borderplants:
            r,c = borderplants.pop(0)
            if r != previousr or c != previousc + 1:
                sides += 1
            previousr, previousc = r, c

        # Left borders
        # keep plants in the region that do not have a neighbor on the left, sort them by column and then by row
        borderplants = sorted(((col, row) for row,col,neighbors in region if LEFT not in neighbors))
        previousr, previousc = -1, -1
        while borderplants:
            c,r = borderplants.pop(0) # column first, row in second position!
            if r != previousr+1 or c != previousc:
                sides += 1
            previousr, previousc = r, c

        # Right borders
        borderplants = sorted(((col, row) for row,col,neighbors in region if RIGHT not in neighbors))
        previousr, previousc = -1, -1
        while borderplants:
            c,r = borderplants.pop(0)
            if r != previousr+1 or c != previousc:
                sides += 1
            previousr, previousc = r, c

        return sides


price = 0
for row in range(rowmax):
    for col in range(colmax):
        if garden[row][col].isupper():
            region = recursiveregion(row, col)
            area = len(region)
            price += area * perimeter(region)
print(price)
