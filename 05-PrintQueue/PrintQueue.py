#! /usr/bin/env python3

import aoc

rules = {}
paragraphs = aoc.Input(split="|", convert=int, groupby="paragraph")
for before, after in next(paragraphs):
    rules.setdefault(before, []).append(after)
paragraphs.split = ","
updates = list(next(paragraphs))


def isok(update, rules):
    for i, page in enumerate(update):
        for nextpage in update[i+1:]:
            if nextpage in rules and page in rules[nextpage]:
                return False
    return True

if aoc.part == "one":
    res = 0
    for update in updates:
        if isok(update, rules):
            n = len(update)
            res += update[(n-1)//2]
    print(res)
# solution: 4637




if aoc.part == "two":
    def restore(update, rules, index):
        firstpage = update[index]
        for j, nextpage in enumerate(update[index+1:]):
                if nextpage in rules and firstpage in rules[nextpage]:
                    update[index] = nextpage
                    update[index+j+1] = firstpage
                    restore(update, rules, index)
                    return
        index += 1
        if index == len(update)-1:
            return
        restore(update, rules, index)

    res = 0
    for update in updates:
        if not isok(update, rules):
            restore(update, rules, 0)
            n = len(update)
            res += update[(n-1)//2]
    print(res)
# solution: 6370
