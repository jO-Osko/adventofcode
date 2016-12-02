DAY = 8

import re

def part1(inp):
    rtr = 0
    for line in inp:
        line = line.strip()
        rtr += len(line) - len(eval(line))
    return rtr

def part2(inp):
    rtr = 0
    for line in inp:
        line = line.strip()
        rtr += len(re.escape(line)) + 2 - len(line)
    return rtr

# To prevent python from auto encoding 
print(part1(open("day8.in")))
print(part2(open("day8.in")))
