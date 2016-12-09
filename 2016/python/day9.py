# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file

DAY = 9

data = get_file(DAY).read().strip()


def part1(data):
    # rtr = ""
    rtr = 0
    j = 0
    L = len(data)
    while j < L:
        c = data[j]
        if c != "(":
            # rtr += c
            rtr += 1
            j += 1
        else:
            i = j + 1
            temp = ""
            le = 0
            while i < L and data[i] != ")":
                if data[i] == "x":
                    le = int(temp)
                    temp = ""
                else:
                    temp += data[i]
                i += 1
            times = int(temp)
            # rtr += data[i+1: i+1+le] * times
            rtr += le * times
            j = i + 1 + le
    return rtr


def part2(data, start_ind=0, end_ind=None):
    if end_ind is None:
        end_ind = len(data)
    rtr = 0
    j = start_ind
    while j < end_ind:
        c = data[j]
        if c != "(":
            rtr += 1
            j += 1
        else:
            i = j + 1
            temp = ""
            le = 0
            while i < end_ind and data[i] != ")":
                if data[i] == "x":
                    le = int(temp)
                    temp = ""
                else:
                    temp += data[i]
                i += 1
            times = int(temp)
            rtr += part2(data, i + 1, i + 1 + le) * times
            j = i + 1 + le
    return rtr

print(part1(data))
print(part2(data))
