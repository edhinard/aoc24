#! /usr/bin/env python3

import itertools

import aoc




if aoc.part == "one":
    #   +---+---+---+
    # 3 | 7 | 8 | 9 |
    #   +---+---+---+
    # 2 | 4 | 5 | 6 |
    #   +---+---+---+
    # 1 | 1 | 2 | 3 |
    #   +---+---+---+
    # 0     | 0 | A |
    #       +---+---+
    #     0   1   2
    def numpad(num, previous):
        if num == previous:
            return [""]
        keypad = {"7": (0,3), "8": (1,3), "9": (2,3),
                  "4": (0,2), "5": (1,2), "6": (2,2),
                  "1": (0,1), "2": (1,1), "3": (2,1),
                              "0": (1,0), "A": (2,0)}
        dx = keypad[num][0] - keypad[previous][0]
        dy = keypad[num][1] - keypad[previous][1]
        hor = (">" if dx > 0 else "<") * abs(dx)
        ver = ("^" if dy > 0 else "v") * abs(dy)
        if previous in "0A" and num in "147":
            return [ver+hor]
        if previous in "147" and num in "0A":
            return [hor+ver]
        #return [hor+ver]
        return list({hor+ver, ver+hor})

    #       +---+---+
    # 1     | ^ | A |
    #   +---+---+---+
    # 0 | < | v | > |
    #   +---+---+---+
    #     0   1   2
    def dirpad(direction, previous):
        if direction == previous:
            return [""]
        keypad = {            "^": (1,1), "A": (2,1),
                  "<": (0,0), "v": (1,0), ">": (2,0)}
        dx = keypad[direction][0] - keypad[previous][0]
        dy = keypad[direction][1] - keypad[previous][1]
        hor = (">" if dx > 0 else "<") * abs(dx)
        ver = ("^" if dy > 0 else "v") * abs(dy)
        if previous in "^A" and direction in ">":
            return [ver+hor]
        if previous in ">" and direction in "^A":
            return [hor+ver]
        #return [hor+ver]
        return list({hor+ver, ver+hor})

    count = 0
    for nums in aoc.Input():
        print()
        print(nums)
        import sys
        minscore = sys.maxsize
        for dirsequences1 in itertools.product(*(numpad(num, previous=previous) for previous, num in itertools.pairwise("A" + nums))):
            dirsequences1 = "A".join(dirsequences1) + "A"  # noqa: PLW2901
            #print(dirsequences1)

            for dirsequences2 in itertools.product(*(dirpad(dir, previous=previous) for previous, dir in itertools.pairwise("A" + dirsequences1))):
                dirsequences2 = "A".join(dirsequences2) + "A"  # noqa: PLW2901
                #print(" " + dirsequences2)

                for dirsequences3 in itertools.product(*(dirpad(dir, previous=previous) for previous, dir in itertools.pairwise("A" + dirsequences2))):
                    dirsequences3 = "A".join(dirsequences3) + "A"  # noqa: PLW2901
                    minscore = min(minscore, len(dirsequences3) * int(nums[:-1]))
                    #print("  " + dirsequences3)
                    #print(len(dirsequences3), int(nums[:-1]))
                    #count += len(dirsequences3) * int(nums[:-1])
        count += minscore
    print(count)

# 188192 too high



if aoc.part == "two":
    NUMROBOT = 26
    robots = [{"A": "A"} for _ in range(NUMROBOT)]

    def findinput(output, robots=robots):
        if not robots:
            return output
        if output not in robots[0]:
            robots[output] = 
        
        return robots[0][output]





