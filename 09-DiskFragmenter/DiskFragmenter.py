#! /usr/bin/env python3

import itertools

import aoc



if aoc.part == "one":
    diskmap = [int(a) for a in aoc.Input().read().strip()]

    def fileidfromend(diskmap):
        position = sum(diskmap) - 1
        index = len(diskmap) - 1
        while index >= 0:
            ID = index // 2
            length = diskmap[index]
            for _ in range(length):
                yield position, ID
                position -= 1
            index -=1
            position -= diskmap[index]
            index -= 1
    fromend = fileidfromend(diskmap)

    def fileidfromstart(diskmap):
        index = 0
        position = diskmap[index]
        while index < len(diskmap):
            index += 1
            length = diskmap[index]
            for _ in range(length):
                yield position, 0
                position += 1

            index +=1
            ID = index // 2
            length = diskmap[index]
            for _ in range(length):
                yield position, ID
                position += 1

    fromstart = fileidfromstart(diskmap)


    checksum = 0
    lastfileid = 0
    fileid = 0
    lastposition = 10000000000000000
    while True:
        position, ID = next(fromstart)
    #        print(f"fromstart {position=} {ID=}")
        if ID:
            fileid = ID
            if lastposition <= position:
                print("start", position, lastposition)
                break
            checksum += position * fileid
            print(position, fileid, checksum)
        else:
            lastposition, lastfileid = next(fromend)
            if lastposition <= position:
                print("end", position, lastposition)
                break
            checksum += position * lastfileid
            print(position, lastfileid, checksum, " --- ", lastposition)
    print(checksum)
# solution: 


if aoc.part == "two":
    res = 0
    print(res)
# solution: 
