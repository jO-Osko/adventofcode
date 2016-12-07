# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from hashlib import md5

from helper import get_file

DAY = 6

data = [line.strip() for line in get_file(DAY)]


def part1(data):
    from collections import Counter
    rtr = ""
    for ch in zip(*data):
        c = Counter(ch)
        rtr += c.most_common(1)[0][0]
    return rtr


def part2(data):
    from collections import Counter
    rtr = ""
    for ch in zip(*data):
        c = Counter(ch)
        rtr += c.most_common(None)[-1][0]
    return rtr


print(part1(data))
print(part2(data))
