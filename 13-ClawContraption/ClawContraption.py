#! /usr/bin/env python3

import aoc
import re


if aoc.part == "one":

    def press(ax,ay,bx,by,px,py):
        for nb in range(min(100, px//bx), -1, -1):
            for na in range(0, min(100,px//ax)+1, 1):
                if px == nb*bx + na*ax and py == nb*by + na*ay:
                    return 3*na + nb
        return 0


        
    res = 0
    for machine in aoc.Input(split=re.compile(r".*?(?P<x>\d+).*?(?P<y>\d+)"), groupby="paragraph"):
        (ax,ay),(bx,by),(px,py) = [(int(x), int(y)) for x,y in machine]
        c = press(ax,ay,bx,by,px,py)
        res+=c
        print(c)
    print(res)


if aoc.part == "two":
    def press(ax,ay,bx,by,px,py):
        px += 10000000000000
        py += 10000000000000
        na = (by*px-bx*py)/(by*ax-bx*ay)
        nb = (ay*px-ax*py)/(ay*bx-ax*by)
        if na == int(na) and nb == int(nb):
            return 3*int(na) + int(nb)
        return 0


        
    res = 0
    for machine in aoc.Input(split=re.compile(r".*?(?P<x>\d+).*?(?P<y>\d+)"), groupby="paragraph"):
        (ax,ay),(bx,by),(px,py) = [(int(x), int(y)) for x,y in machine]
        c = press(ax,ay,bx,by,px,py)
        res+=c
        print(c)
    print(res)


#!415714979121903984