#! /usr/bin/env python3

import re

import aoc

# The instructions can be understood as:
# find, if they exist, the two integers na and nb so that
#      ->      ->   ->
#   na.A  + nb.B  = P
# with the two variants:
#  - part 1:
#    na and nb should be no more than 100
#  - part 2:
#    ->                         ->  ->
#    P is added 10000000000000.(i + j)
tokens = 0
for (Ax,Ay),(Bx,By),(Px,Py) in aoc.Input(split=re.compile(r"(\d+).*?(\d+)"), convert=int, groupby="paragraph"):
    if aoc.part == "two":
        Px += 10000000000000  # noqa: PLW2901
        Py += 10000000000000  # noqa: PLW2901
    # finding
    a = (By*Px - Bx*Py) / (By*Ax - Bx*Ay)
    b = (Ay*Px - Ax*Py) / (Ay*Bx - Ax*By)
    if not (((na:=int(a)) == a) and ((nb:=int(b)) == b)):
        continue
    if aoc.part == "one" and (na > 100 or nb > 100):  # noqa: PLR2004
        continue
    tokens += 3*na + nb
print(tokens)
