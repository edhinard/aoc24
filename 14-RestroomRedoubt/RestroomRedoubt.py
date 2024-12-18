#! /usr/bin/env python3

import re

import aoc
from PIL import Image, ImageDraw

WIDTH,HEIGHT = (11,7) if aoc.test else (101,103)

robotre = re.compile(r"(-?\d+),(-?\d+).*?(-?\d+),(-?\d+)")
robots = [[px,py,vx,vy] for px,py,vx,vy in aoc.Input(split=robotre, convert=int)]


if aoc.part == "one":
    # Move the robots 100 times each
    for robot in robots:
        px,py,vx,vy = robot
        robot[0] = (px + 100 * vx) % WIDTH
        robot[1] = (py + 100 * vy) % HEIGHT

    # Count the number of robots in each quadrant
    def count(x,y):
        count = 0
        for px,py,_,_ in robots:
             if px==x and py==y:
                 count += 1
        return count

    A,B,C,D = 0,0,0,0
    for x in range(WIDTH // 2):
        for y in range(HEIGHT//2):
            A += count(           x,            y)
            B += count(WIDTH//2+1+x,            y)
            C += count(WIDTH//2+1+x,HEIGHT//2+1+y)
            D += count(           x,HEIGHT//2+1+y)
    print(A*B*C*D)


if aoc.part == "two":
    def move():
        for robot in robots:
            px,py,vx,vy = robot
            robot[0] = (px + vx) % WIDTH
            robot[1] = (py + vy) % HEIGHT

    NUM_COL = 20
    NUM_ROW = 10
    imagenum = 0
    nummove = 0
    while nummove < WIDTH*HEIGHT:
        print(f"drawing moves {nummove} to {min(nummove + NUM_ROW*NUM_COL - 1, WIDTH*HEIGHT)}")
        backgroundcolor = "white"
        im = Image.new("RGB", (NUM_COL*(WIDTH+3),NUM_ROW*(HEIGHT+3)), color=backgroundcolor)
        draw = ImageDraw.Draw(im)
        for row in range(NUM_ROW):
            for col in range(NUM_COL):
                if nummove > WIDTH*HEIGHT:
                    continue
                left = col*(WIDTH+3)
                right = left + WIDTH + 1
                top = row*(HEIGHT+3)
                bottom = top + HEIGHT + 1
                draw.line((left, top, right, top), fill="black")
                draw.line((left, bottom, right, bottom), fill="black")
                draw.line((left, top, left, bottom), fill="black")
                draw.line((right, top, right, bottom), fill="black")
                for x,y,_,_ in robots:
                    draw.point((left + 1 + x, top + 1 + y), "red")
                draw.text((left + 2, top+1), f"{nummove}", fill="blue")
                move()
                nummove += 1
        im.save(f"im{imagenum:02}.png")
        print(f" --> im{imagenum:02}.png\n")
        imagenum += 1
