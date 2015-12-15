DAY = 15

from operator import mul
from functools import reduce


def solve(data, diet=False, callories=500):
    cookies = []
    for part in data:
        part = part.split(":")
        numbers = part[1].strip().split(",")
        cookies.append( [int(j.strip().split(" ")[1]) for j in numbers])

    ma = 0
    def next_perm(ind, left, current):
        if ind == len(cookies)-1: #last one
            cur = [current[i] + cookies[ind][i]*left for i in range(len(current))]
            if diet and cur[-1] != callories:
                return
            nonlocal ma
            mul = 1
            for k in cur[:-1]:
                if k <= 0:
                    return
                mul *= k
            ma = max(ma, mul)
            return
        for j in range(left):
            next_perm(ind+1, left-j, [current[i] + cookies[ind][i]*j for i in range(len(current))])
        
        
    next_perm(0,100,[0 for j in range(len(cookies[0]))])
    
    return ma


def part1(data):
    return solve(data.split("\n"))

def part2(data):
    return solve(data.split("\n"), True)

TEST = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""


DATA = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""

print(part1(DATA))

print(part2(DATA))
