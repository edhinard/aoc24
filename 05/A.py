#! /usr/bin/env python3

import re

import aoc

def isok(update, rules):
        for i, page in enumerate(update):
            for next in update[i+1:]:
                if next in rules and page in rules[next]:
                    return False
        return True

if aoc.part == "one":
    res = 0

    rules = {}
    input = aoc.Input(split="|", convert=int)
    for rule in input:
        if not rule:
            break
        a, b = rule
        rules.setdefault(a, []).append(b)

    input.split = ","
    for update in input:
        if isok(update, rules):
            n = len(update)
            res += update[(n-1)//2]
    print(res)
# solution: 


def swapnok(update, rules):
    for i, page in enumerate(update):
        for j, next in enumerate(update[i+1:]):
            if next in rules and page in rules[next]:
                update[i] = next
                update[i+j+1] = page
                return

if aoc.part == "two":
    res = 0
    rules = {}
    input = aoc.Input(split="|", convert=int)
    for rule in input:
        if not rule:
            break
        a, b = rule
        rules.setdefault(a, []).append(b)
    print(rules)
    input.split = ","
    for update in input:
        if not isok(update, rules):
            while not isok(update, rules):
                #print(update)
                swapnok(update, rules)
                #print(update)
                #import sys
                #sys.exit()
            n = len(update)
            res += update[(n-1)//2]

    print(res)
# solution: 
