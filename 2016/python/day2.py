# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file

DAY = 2

data = get_file(DAY).read()


def part1(data):
    x, y = 1, 1
    key = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    rtr = []
    for line in data.split("\n"):
        line = line.strip()
        if not line:
            break
        for c in line:
            if c == "U":
                y = max(0, y - 1)
            if c == "D":
                y = min(2, y + 1)
            if c == "L":
                x = max(0, x - 1)
            if c == "R":
                x = min(2, x + 1)
        rtr.append(str(key[y][x]))
    return "".join(rtr)


def part2(data, dst=2):
    x, y = 0, 0
    key = [None, None, 1, None, None], [None, 2, 3, 4, None], [5, 6, 7, 8, 9], \
          [None, "A", "B", "C", None], [None, None, "D", None, None]
    rtr = []
    for line in data.split("\n"):
        line = line.strip()
        if not line:
            break
        for c in line:
            if c == "U":
                if abs(y - 1) + abs(x) <= dst:
                    y -= 1
            if c == "D":
                if abs(y + 1) + abs(x) <= dst:
                    y += 1
            if c == "L":
                if abs(x - 1) + abs(y) <= dst:
                    x -= 1
            if c == "R":
                if abs(x + 1) + abs(y) <= dst:
                    x += 1
        rtr.append(str(key[y+dst][x+dst]))
    return "".join(rtr)


print(part1(data))
print(part2(data))
