import argparse
import contextlib
import pathlib
import re


def _init():
    description = "Advent of code 2024"
    parentdirname = pathlib.Path().absolute().name
    if m := re.match(r"(\d+)", parentdirname):
        day = int(m.group(1))
        description += f"\n solution for Day #{day}\n https://adventofcode.com/2022/day/{day}"
    parser = argparse.ArgumentParser(description=description,
                                           formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("part", choices=(1, 2), type=int, help="part")
    parser.add_argument("--test", "-t", action="store_true", help="work on 'test.txt' instead of 'input.txt'")
    args = parser.parse_args()
    path = pathlib.Path("test.txt") if args.test else pathlib.Path("input.txt")
    if not path.exists():
        parser.error(f"missing input file '{path}'")
    if not path.open().read():
        parser.error(f"empty input file '{path}'")
    return "one" if args.part == 1 else "two", path, args.test

part, path, test = _init()

class Input:
    class NoSplit:
        pass

    def __init__(self, *, split=NoSplit, convert=None, groupby=None):
        self.file = path.open()
        self.split = split
        self.convert = convert
        self.groupby = groupby
        self.eof = False

    def read(self):
        return self.file.read()

    def nextline(self, *, emptyisnone=False):
        try:
            line = next(self.file)
        except StopIteration:
            self.eof = True
            raise
        stripped = line[:-1] if line.endswith("\n") else line
        if stripped:
            return self.lineconvert(stripped)
        if emptyisnone:
            return None
        return ""

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            raise StopIteration

        match self.groupby:
            case None:
                return self.nextline()
            case int():
                return tuple([self.nextline() for _ in range(self.groupby)])
            case "paragraph":
                return self.paragraph()

    def paragraph(self):
        while not self.eof:
            try:
                line = self.nextline(emptyisnone=True)
            except StopIteration:
                return
            if line is None:
                return
            yield line

    def lineconvert(self, line):
        if isinstance(self.split, re.Pattern):
            items = m.groups() if (m := self.split.match(line)) else [line]
        elif self.split == "":
            items = list(line)
        elif isinstance(self.split, str):
            items = line.split(self.split)
        elif self.split == Input.NoSplit:
            items = [line]
        elif self.split is None:
            items = line.split()
        else:
            raise ValueError(f"bad value for split={self.split}")

        if self.convert:
            for i, item in enumerate(items[:]):
                with contextlib.suppress(Exception):
                    items[i] = self.convert(item)

        if self.split == Input.NoSplit:
            return items[0]
        return items
