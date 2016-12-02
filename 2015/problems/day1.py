DAY = 1

def part1(data):
    return sum(1 if j == "(" else -1 for j in data.strip())

def part2(data):
    curr = 0
    for i,c in enumerate(data.strip()):
        if c == "(":
            curr += 1
        else:
            curr -= 1
            if curr == -1:
                return i+1
