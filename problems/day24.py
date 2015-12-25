DAY = 24

from functools import lru_cache, reduce
from operator import mul
from itertools import combinations


def part1(data):
    return solve([int(j) for j in data.split("\n")])

def solve(data, parts=3):
    su = sum(data)
    part = su//parts

    comb = [j for j in range(len(data))]

    mi = float("inf")

    for j in range(1, len(data)):
        for comb in combinations(data, j):
            if sum(comb) == part:
                mi = min(reduce(mul, comb), mi)
        if mi < float("inf"):
            return mi


def part2(data):
    return solve([int(j) for j in data.split("\n")], 4)



DATA = """1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113"""

print(part1(DATA))
print(part2(DATA))
