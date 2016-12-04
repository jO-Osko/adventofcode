# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file

DAY = 4

data = [line.strip()[:-1].split("[") for line in get_file(DAY)]


def part1(data):
    from collections import Counter
    su = 0
    for line in data:
        dat, uid = line[0].rsplit("-", 1)
        dat = dat.replace("-", "")
        checksum = line[1]
        c = Counter(dat)
        d = c.most_common()
        d.sort(key=lambda x: (-x[1], x[0]))

        if "".join([j[0] for j in d[:5]]) == checksum:
            su += int(uid)
    return su



def part2(data):
    circ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    for line in data:
        dat, uid = line[0].rsplit("-", 1)

        name = "".join([circ[(circ.index(j) + int(uid)) % 26] if j != "-" else " " for j in dat])

        if name == "northpole object storage":
            return uid


print(part1(data))
print(part2(data))
