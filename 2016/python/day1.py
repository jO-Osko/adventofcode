# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file

DAY = 1

data = get_file(DAY).read().split(",")


def part1(data):
    direction = 1
    location = [0, 0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def rotate(direction, change):
        return (direction + [-1, 1][change == "L"]) % 4

    for step in data:
        change, *dst = step.strip()
        dst = int("".join(dst))
        direction = rotate(direction, change)
        dir_vec = directions[direction]
        location[0] += dir_vec[0] * dst
        location[1] += dir_vec[1] * dst

    return sum(map(abs, location))


def part2(data):
    direction = 1
    location = [0, 0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    hq = None
    visited = set()

    def rotate(direction, change):
        return (direction + [-1, 1][change == "L"]) % 4

    for step in data:
        change, *dst = step.strip()
        dst = int("".join(dst))
        direction = rotate(direction, change)
        dir_vec = directions[direction]
        for j in range(dst):
            location[0] += dir_vec[0]
            location[1] += dir_vec[1]
            if hq is None and tuple(location) in visited:
                return sum(map(abs, location))
            visited.add(tuple(location))

print(part1(data))
print(part2(data))
