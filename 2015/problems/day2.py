DAY = 2

from operator import mul

def calculate(dimensions):
    dimensions = map(int, dimensions.split("x"))
    sides = dimensions[0]*dimensions[1], dimensions[0]*dimensions[2], dimensions[1]*dimensions[2]

    return 2 * sum(sides) + min(sides)
    

def part1(data):
    return sum(calculate(dim) for dim in data.split("\n"))


def calculate2(dimensions):
    dimensions = map(int, dimensions.split("x"))
    dimensions.sort()
    return 2*(dimensions[0] + dimensions[1]) + reduce(mul, dimensions)
    
def part2(data):
    return sum(calculate2(dim) for dim in data.split("\n"))
