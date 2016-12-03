# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file

DAY = 3

data = [list(map(int, line.strip().split())) for line in get_file(DAY)]


def part1(data):
    return sum(all([a + b > c, a + c > b, c + b > a]) for a, b, c in data)


def part2(data):
    fst, snd, trd = [], [], []
    for x, y, z in data:
        fst.append(x)
        snd.append(y)
        trd.append(z)
    data = fst + snd + trd
    return part1([[data[j], data[j+1], data[j+2]] for j in range(0, len(data), 3)])


print(part1(data))
print(part2(data))
