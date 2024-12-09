#! /usr/bin/env python3

import dataclasses
import typing

import aoc

if aoc.part == "one":
    diskmap = [int(a) for a in aoc.Input().read().strip()]

    # Iterator over file blocks in disk map from end to start
    # yields: (position, fileID)
    def fileblocksfromend(diskmap):
        index = len(diskmap) - 1
        position = sum(diskmap) - 1
        while index >= 0:
            ID = index // 2
            length = diskmap[index]
            for _ in range(length):
                yield position, ID
                position -= 1
            index -=1

            # skip space blocks
            position -= diskmap[index]
            index -= 1
    fileblocksfromend = fileblocksfromend(diskmap)

    # Iterator over space blocks in disk map
    # yields: position
    def spaceblocksfromstart(diskmap):
        index = 0
        position = 0
        while index < len(diskmap)-1:
            # skip file blocks
            position += diskmap[index]
            index += 1

            length = diskmap[index]
            for _ in range(length):
                yield position
                position += 1
            index +=1
        while True:
            yield sum(diskmap)
    spaceblocksfromstart = spaceblocksfromstart(diskmap)

    checksum = 0
    for fileposition, fileid in fileblocksfromend:
        spaceposition = next(spaceblocksfromstart)
        if spaceposition < fileposition:
            # file block can be copied into space block => update checksum with space position
            checksum += spaceposition * fileid
        else:
            # no space left to copy file block => update checksum with current file position
            checksum += fileposition * fileid
    print(checksum)
# solution: 6519155389266


if aoc.part == "two":
    # convert entry line into a list of space block chunks (id = None) and file block chunks (id ≠ None)
    @dataclasses.dataclass
    class Chunk:
        currentposition: typing.ClassVar = 0
        currentid: typing.ClassVar = 0
        isfile: typing.ClassVar = True
        position: int
        id: int | None
        length: int

        def __init__(self, length):
            self.position = Chunk.currentposition
            if Chunk.isfile:
                self.id = Chunk.currentid
                Chunk.currentid += 1
                Chunk.isfile = False
            else:
                self.id = None
                Chunk.isfile = True
            self.length = length
            Chunk.currentposition += length
    chunks = [Chunk(int(length)) for length in aoc.Input().read().strip()]

    checksum = 0
    while chunks:
        # pop the last memory chunk from list
        chunk = chunks.pop()

        # if it is a space, skip it
        if chunk.id is None:
            continue

        # it is a file
        filechunk = chunk

        # find the first space chunk big enough to contain the whole file
        for spacechunk in [chunk for chunk in chunks if chunk.id is None]:
            if spacechunk.length >= filechunk.length:

                # move the file into the space (just update the checksum and adjust the space position and length)
                for _ in range(filechunk.length):
                    checksum += spacechunk.position * filechunk.id
                    spacechunk.position += 1
                    spacechunk.length -= 1
                break

        # no space large enough to contain the file was found
        else:
            # update the checksum for the unmodified file
            for _ in range(filechunk.length):
                checksum += filechunk.position * filechunk.id
                filechunk.position += 1
    print(checksum)
# solution: 6547228115826
