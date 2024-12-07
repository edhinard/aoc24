#! /usr/bin/env python3

import aoc

if aoc.part == "one":
    operators = ("*", "+")
# solution: 5030892084481


if aoc.part == "two":
    operators = ("*", "+", "")
# solution: 91377448644679

def canbetrue(result, numbers, operators):
    if len(numbers) == 1:
        return result == numbers[0]
    for op in operators:
        num0 = eval(f"{numbers[0]}{op}{numbers[1]}")  # noqa: S307
        if canbetrue(result, [num0, *numbers[2:]], operators):
            return True
    return False

res = 0
for equationresult, equationumbers in aoc.Input(split=":"):
    result = int(equationresult)
    numbers = [int(n) for n in equationumbers.split()]
    if canbetrue(result, numbers, operators):
        res += result
print(res)
