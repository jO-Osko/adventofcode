DAY = 3

def calculate1(path):
    visited = {(0,0)}
    last = (0,0)
    for c in path:
        x,y = last
        if c == "<":
            last = x-1, y
        elif c == ">":
            last = x+1,y
        elif c == "v":
            last = x, y-1
        else:
            last = x, y+1
        visited.add(last)
    return visited

def part1(data):
    return len(calculate1(data))


def calculate2(data):
    santa = "".join(data[j] for j in range(0, len(data),2))
    robot = "".join(data[j] for j in range(1, len(data),2))
    return calculate1(santa) | calculate1(robot)
    
def part2(data):
    return len(calculate2(data))
