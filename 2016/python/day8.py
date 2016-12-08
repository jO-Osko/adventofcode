# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file

DAY = 8

HEIGHT = 6
WIDTH = 50

data = [line.strip() for line in get_file(DAY)]


def part1(data):
    screen = [["." for k in range(WIDTH)] for j in range(HEIGHT)]
    for line in data:
        cmd, *rest = line.split(" ", 1)
        if cmd == "rect":
            A, B = map(int, rest[0].split("x"))
            A %= WIDTH
            B %= HEIGHT
            for j in range(B):
                screen[j][0:A] = "#"*A
            continue
        rest = rest[0].split(" ")
        B = int(rest[-1])
        A = int(rest[1].split("=")[-1])
        if rest[0].startswith("row"):
            B %= WIDTH
            temp = [k for k in screen[A]]
            for j in range(WIDTH):
                screen[A][(j + B) % WIDTH] = temp[j]
        else:
            B %= HEIGHT
            temp = [screen[j][A] for j in range(HEIGHT)]
            for j in range(HEIGHT):
                screen[(j + B) % HEIGHT][A] = temp[j]

    su = 0
    for j in screen:
        print("".join(j))
        for k in j:
            if k == "#":
                su += 1

    return su



def part2(data):
    screen = [["." for k in range(WIDTH)] for j in range(HEIGHT)]
    for line in data:
        cmd, *rest = line.split(" ", 1)
        if cmd == "rect":
            A, B = map(int, rest[0].split("x"))
            A %= WIDTH
            B %= HEIGHT
            for j in range(B):
                screen[j][0:A] = "#"*A
            continue
        rest = rest[0].split(" ")
        B = int(rest[-1])
        A = int(rest[1].split("=")[-1])
        if rest[0].startswith("row"):
            B %= WIDTH
            temp = [k for k in screen[A]]
            for j in range(WIDTH):
                screen[A][(j + B) % WIDTH] = temp[j]
        else:
            B %= HEIGHT
            temp = [screen[j][A] for j in range(HEIGHT)]
            for j in range(HEIGHT):
                screen[(j + B) % HEIGHT][A] = temp[j]

    rtr = ""
    for j in screen:
        rtr += "".join(j) + "\n"


    return rtr



print(part1(data))
print(part2(data))
