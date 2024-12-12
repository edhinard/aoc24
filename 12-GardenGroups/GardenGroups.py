#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    garden = list(aoc.Input(split=""))
    rowmax = len(garden)
    colmax = len(garden[0])

    def neighbours(row, col):
        neigh = []
        plant = garden[row][col]
        for r,c in ((row-1, col), (row, col+1), (row+1,col), (row,col-1)):
            if r>=0 and r<rowmax and c>=0 and c<colmax and garden[r][c] == plant:
                neigh.append((r,c))
        return neigh

    def recursiveregion(row, col, area=0):
        if garden[row][col] == ".":
            return area, 0
        area += 1
        neigh = neighbours(row, col)
        neighcount = len(neigh)
        garden[row][col] = "."
        for r,c in neigh:
            area, n = recursiveregion(r, c, area)
            neighcount += n
        return area, neighcount

    def regionprices():
        for row in range(rowmax):
            for col in range(colmax):
                if garden[row][col] != ".":
                    area, neighcount = recursiveregion(row, col)
                    perimeter = area * 4 - neighcount * 2
                    price = area * perimeter
                    yield price

    print(sum(price for price in regionprices()))

if aoc.part == "two":
    pass
