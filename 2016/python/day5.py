# -*- coding: utf-8 -*-

__author__ = "Filip Koprivec"

from hashlib import md5

from helper import get_file

DAY = 5

data = get_file(DAY).read().strip()


def part1(data):
    rtr = ""
    a = 0
    while len(rtr) < 8:
        if md5((data + str(a)).encode("utf-8")).hexdigest().startswith("00000"):
            rtr += md5((data + str(a)).encode("utf-8")).hexdigest()[5]
        a += 1
    return rtr


def part2(data):
    rtr = ["" for j in range(8)]
    n = 0
    a = 0
    while n < 8:
        if md5((data + str(a)).encode("utf-8")).hexdigest().startswith("00000"):
            ha = md5((data + str(a)).encode("utf-8")).hexdigest()
            if ha[5].isdigit() and int(ha[5]) < 8 and not rtr[int(ha[5])]:
                rtr[int(ha[5])] += ha[6]
                n += 1
        a += 1
    return "".join(rtr)


print(part1(data))
print(part2(data))
