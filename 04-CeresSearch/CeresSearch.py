#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    def xmascount(page, row, col):
        height = len(page)
        width = len(page[0])
        if page[row][col] != "X":
            return 0
        count = 0
        # find XMAS around the current X
        if page[row][col:].startswith("XMAS"):
            count += 1 # rightwards
        if page[row][:col+1].endswith("SAMX"):
            count += 1 # leftwards
        if row <= height-4:
            if page[row+1][col] == "M" and page[row+2][col] == "A" and page[row+3][col] == "S":
                count += 1 # downwards
            if col <= width-4 and page[row+1][col+1] == "M" and page[row+2][col+2] == "A" and page[row+3][col+3] == "S":
                count += 1 # downrightwards
            if col >= 3 and page[row+1][col-1] == "M" and page[row+2][col-2] == "A" and page[row+3][col-3] == "S":  # noqa: PLR2004
                count += 1 # downleftwards
        if row >= 3:  # noqa: PLR2004
            if page[row-1][col] == "M" and page[row-2][col] == "A" and page[row-3][col] == "S":
                count += 1 # upwards
            if col <= width-4 and page[row-1][col+1] == "M" and page[row-2][col+2] == "A" and page[row-3][col+3] == "S":
                count += 1 # uprightwards
            if col >= 3 and page[row-1][col-1] == "M" and page[row-2][col-2] == "A" and page[row-3][col-3] == "S":  # noqa: PLR2004
                count += 1 # upleftwards
        return count
# solution: 2336


if aoc.part == "two":
    def xmascount(page, row, col):
        height = len(page)
        width = len(page[0])
        if page[row][col] != "A":
            return 0
        if row == 0 or row == height-1 or col == 0 or col == width-1:
            return 0
        # find the two crossed MAS around the current A
        corners = page[row-1][col-1] + page[row-1][col+1] + page[row+1][col+1] + page[row+1][col-1]
        if corners in ["MMSS", "SMMS", "SSMM", "MSSM"]:
            return 1
        return 0
# solution: 1831

page = list(aoc.Input())
height = len(page)
width = len(page[0])
print(sum(xmascount(page, r, c) for r in range(width) for c in range(height)))
