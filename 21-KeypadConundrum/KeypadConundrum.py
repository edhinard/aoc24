#! /usr/bin/env python3

import collections
import functools
import itertools

import aoc

#  Numeric Keypad
#   +---+---+---+
# 3 | 7 | 8 | 9 |
#   +---+---+---+
# 2 | 4 | 5 | 6 |   Directional Keypad
#   +---+---+---+          +---+---+
# 1 | 1 | 2 | 3 |    1   ! | ^ | * | <- activate button renamed /!\
#   +---+---+---+      +---+---+---+
# 0   ! | 0 | A |    0 | < | v | > |    "!" is the forbidden key above which the arm must not go
#       +---+---+      +---+---+---+
#     0   1   2          0   1   2
Key = collections.namedtuple("Key", "r c")
numerickeypad = {key: Key(r, c) for r, row in enumerate(("!0A", "123", "456", "789")) for c, key in enumerate(row)}
directionalkeypad = {key: Key(r, c) for r, row in enumerate(("<v>", "!^*")) for c, key in enumerate(row)}

def robotsequence(position1, position2):
    # Returns one or two key sequence on a robot directional keypad in order to move his arm
    # from position1 to position2 and press (both positions given as key symbols which determine the target keypad)
    keypad = numerickeypad if position1 in "0123456789A" else directionalkeypad
    dr = (r2 := keypad[position2].r) - (r1 := keypad[position1].r)
    dc = (c2 := keypad[position2].c) - (c1 := keypad[position1].c)
    updownsubsequence = "v^"[dr > 0] * abs(dr)
    leftrightsubsequence = "<>"[dc > 0] * abs(dc)
    if (r1, c2) == keypad["!"]:
        # cannot start with left-right sub-sequence since it goes through forbidden key
        return (updownsubsequence+leftrightsubsequence+"*",)
    if (r2, c1) == keypad["!"]:
        # cannot start with up-down sub-sequence since it goes through forbidden key
        return (leftrightsubsequence+updownsubsequence+"*",)
    # both sequence are allowed: left-right sub-sequence followed by up-down sub-sequence and the opposite,
    #  but since they can be identical if one or the other is empty, a set is used to keep only one in that case
    return tuple({leftrightsubsequence+updownsubsequence+"*", updownsubsequence+leftrightsubsequence+"*"})


@functools.cache
def lengthofminimalsequence(sequence, keypadindex):
    # Returns the length of the shortest key sequence on keypad #keypadindex
    #  that generates the input sequence on keypad #numberofkeypad
    if keypadindex == numberofkeypad:
        return len(sequence)
    activatekey = "A" if keypadindex == 1 else "*"
    res = 0
    for position1, position2 in itertools.pairwise(activatekey + sequence):
        res += min(lengthofminimalsequence(seq, keypadindex+1) for seq in robotsequence(position1, position2))
    return res


if aoc.part == "one":
    numberofkeypad = 4

if aoc.part == "two":
    numberofkeypad = 27


complexity = sum(lengthofminimalsequence(doorcode, 1) * int(doorcode[:-1]) for doorcode in aoc.Input())
print(complexity)
