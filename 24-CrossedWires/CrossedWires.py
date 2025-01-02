#! /usr/bin/env python3

import re

import aoc

paragraphs = aoc.Input(groupby="paragraph")
paragraphs.convert = int
paragraphs.split = ": "
XY = []
for xy, value in next(paragraphs):
    XY.append((xy, value))

# xnn and ynn input values are sorted by nn
XY.sort(key=lambda item: item[0][1:])

paragraphs.split = re.compile(r"(\S+) (\S+) (\S+) -> (\S+)")
gates = list(next(paragraphs))


# Compute the output value of all gates
# Keep the order of activation of each gate in an ordered cells list
#  a cell is a list of gates activated by the same xnn and ynn
cells = []
cellgates = []
# start with an empty list of values
values = {}
while gates:
    # add the first available XY input value (x00 then y00 then x01 then y01 ...)
    xy, value = XY.pop(0)
    values[xy] = value

    # find all gates whose output value can be computed (given the already known values)
    while True:
        for i, gate in enumerate(gates):
            in1, op, in2, out = gate
            if in1 in values and in2 in values:
                # this gate output can be computed
                match op:
                    case "AND":
                        value = values[in1] & values[in2]
                    case "XOR":
                        value = values[in1] ^ values[in2]
                    case "OR":
                        value = values[in1] | values[in2]

                # remove the gate from the list
                # update the values
                gates.pop(i)
                values[out] = value
                cellgates.append(gate)
                break
        else:
            break

    # no more gates can be activated, need some new input values
    if cellgates:
        cells.append(cellgates)
        cellgates = []


if aoc.part == "one":
    # In that part, only the znn values are of interest
    Z = 0
    for z in sorted((name for name in values if name.startswith("z")), key=lambda name: name[1:], reverse=True):
        Z = Z * 2 + values[z]
    print(f"{Z=}")


if aoc.part == "two":
    # Each cell is a 1 bit additionner with following structure:
    #   xn o----+--*
    #           |  XOR*--+----*
    #   yn o-+-----*     |     XOR*--o zn
    # cn-1 o-----------+------*
    #        |  |      | |
    #        |  |      | *
    #        |  |      | AND*--+
    #        |  +--*   +-*     |
    #        |     AND*------+ |
    #        +-----*         | |
    #                        | *
    #                        |  OR*--o cn
    #                        +-*
    #
    # We are finding 4 cells with anomalies
    #  in my input I already know (after visual analysis) that there are 2 kind of anomalies:
    #   - the first xor output is not reused in the second one (xor with the previous carry)
    #   - the second xor output is not zn

    # first cell is simpler:
    #   x0 o----+--*
    #           |  XOR*--o z0
    #   y0 o-+-----*
    #        |  |
    #        |  +--*
    #        |     AND*--o c1
    #        +-----*
    gates = cells.pop(0)
    possiblecarry = [out for _, op, _, out in gates]

    swapped = []
    for num, gates in enumerate(cells, start=1):
        xor1, xor2, and1, and2, or1 = sorted(gates, key=lambda g: {"XOR": 0, "AND": 1, "OR": 2}[g[1]])
        _, _, _, xXy = xor1
        in1, _, in2, out2 = xor2

        # first possible anomaly: xn XOR yn (==result of first xor) is not xored with previous carry
        intermediate = in1 if in2 in possiblecarry else in2
        if xXy != intermediate:
            swapped.append(intermediate)
            swapped.append(xXy)

        # second possible anomaly: carry XOR xXy (result of second xor) is not zn
        zn = f"z{num:02}"
        if out2 != zn:
            swapped.append(out2)
            swapped.append(zn)

        # store carry for next cell
        possiblecarry = [out for _, op, _, out in gates]

    print(",".join(sorted(swapped)))
