# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from helper import get_file
import re

DAY = 7

data = [line.strip() for line in get_file(DAY)]


def part1(data):
    def check(x):
        return x is not None and x.group()[0] != x.group()[1]
    n = 0
    reg = "(.)(.)\\2\\1"
    for line in data:
        ins, ous = [], []
        spl = line.split("]")
        for j in spl:
            if "[" not in j:
                ins.append(j)
                break
            bef, aft = j.split("[")
            ins.append(bef)
            ous.append(aft)
        if any(map(lambda x: check(re.search(reg, x)), ins)) and not any(map(lambda x: check(re.search(reg, x)), ous)):
            n += 1
    return n




def part2(data):
    def find(ous):
        rtr = []
        for j in ous:
            for k in range(len(j)-2):
                m = j[k:k+3]
                if m[0] == m[2] and m[1] != m[0]:
                    rtr.append(m)
        return rtr

    def check(s, ins):
        s = s[1] + s[0] + s[1]
        for j in ins:
            if s in j:
                return True
        return False

    n = 0
    for line in data:
        ins, ous = [], []
        spl = line.split("]")
        for j in spl:
            if "[" not in j:
                ins.append(j)
                break
            bef, aft = j.split("[")
            ins.append(bef)
            ous.append(aft)
        if any(check(j, ins) for j in find(ous)):
            n += 1

    return n



print(part1(data))
print(part2(data))
