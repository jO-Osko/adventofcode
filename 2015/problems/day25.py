DAY = 25


def part1(data):
    row, col = data.split("\n")
    return solve(int(row), int(col))

def part2(data):
    import os
    return os.system("SUDO START WEATHER MACHINE")
    

def get_num(row, col):
    num = row + col -2
    return (num * (num + 1)) // 2 + col - 1 # Thanks Pretnar :)

def solve(row, col, start=20151125, a=252533, mod=33554393):

    return (pow(a, get_num(row, col), mod) * start) % mod


DATA = """3010
3019"""


print(part1(DATA))
