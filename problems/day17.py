DAY = 17

from functools import lru_cache

def part1(data, limit=150):
    return solve(data.strip().split("\n"),limit)

def part2(data, limit=150):
    return solve(data.strip().split(), limit, True)

part2_solution = None

def solve(data, limit, second=False):
    data = [int(j) for j in data]

    if second: #because I can :)
        try:
            return solve.min_taken
            
        except:
            solve(data, limit)
            return solve.min_taken 

    solve.min_len = float("inf")
    solve.min_taken = 0

    # second doesnt work with simple memo
    #@lru_cache(maxsize=None)
    def fill(ind, left, taken=0):
        if left == 0:
            if taken < solve.min_len:
                solve.min_len = taken
                solve.min_taken = 0
            if taken == solve.min_len:
                solve.min_taken += 1
            return 1
        if ind == len(data):
            return 0

        return sum(fill(j+1, left-data[j], taken+1) for j in range(ind, len(data)))

    rtr = fill(0,limit)
    return rtr


DATA = """50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40"""
print(part1(DATA))
print(part2(DATA))
