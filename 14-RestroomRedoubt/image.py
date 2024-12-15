#! /usr/bin/env python3

import re

import aoc
from PIL import Image, ImageDraw

WIDTH=101
HEIGHT=103

robots = [[px,py,vx,vy] for px,py,vx,vy in aoc.Input(split=re.compile(r"(-?\d+),(-?\d+).*?(-?\d+),(-?\d+)"), convert=int)]
def move():
    for robot in robots:
        px,py,vx,vy = robot
        robot[0] = (px + vx) % WIDTH
        robot[1] = (py + vy) % HEIGHT
def count(x,y):
    count = 0
    for px,py,_,_ in robots:
         if px==x and py==y:
             count += 1
    return count

IMAGE_WIDTH = 20
IMAGE_HEIGHT = 10
num = 0

def image(n):
    global num
    backgroundcolor = "white"
    im = Image.new("RGB", (IMAGE_WIDTH*(WIDTH+3),IMAGE_HEIGHT*(HEIGHT+3)), color=backgroundcolor)
    draw = ImageDraw.Draw(im)
    for j in range(IMAGE_HEIGHT):
        for i in range(IMAGE_WIDTH):
            left = i*(WIDTH+3)
            right = left + WIDTH + 1
            top = j*(HEIGHT+3)
            bottom = top + HEIGHT + 1
            draw.line((left, top, right, top), fill="black")
            draw.line((left, bottom, right, bottom), fill="black")
            draw.line((left, top, left, bottom), fill="black")
            draw.line((right, top, right, bottom), fill="black")
            for x in range(WIDTH):
                for y in range(HEIGHT):
                    if count(x, y):
                        draw.point((left + 1 + x, top + 1 + y), "red")
            draw.text((left + 2, top+1), f"{num}", fill="blue")
            move()
            num += 1
    im.save(f"im{n}.png")
for n in range(200):
    print(n)
    image(n)
