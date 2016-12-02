DAY = 6

def part1(data):
    table = [[0 for j in range(1000)] for i in range(1000)]
    solve_part(table, data.split("\n"))
    return sum(map(sum, table))

def part2(data):
    table = [[0 for j in range(1000)] for i in range(1000)]
    solve_part(table, data.split("\n"), smart=1)
    return sum(map(sum, table))


def toogle(x1,x2,y1,y2,table, smart=0):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if smart:
                table[x][y] += 2
            else:
                table[x][y] = not table[x][y]

def turn_off(x1,x2,y1,y2,table, smart=0):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if smart:
                table[x][y] = max(table[x][y] - 1, 0)
            else:
                table[x][y] = 0

def turn_on(x1,x2,y1,y2,table, smart=0):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if smart:
                table[x][y] += 1
            else:
                table[x][y] = 1

def solve_part(table, data, smart=0):
    for part in data:
        *typ, start, through, stop = part.split()
        x1,y1 = map(int, start.split(","))
        x2,y2 = map(int, stop.split(","))
        if typ == ["toggle"]:
            toogle(x1,x2,y1,y2, table, smart)
        elif typ[-1] == "off":
            turn_off(x1,x2,y1,y2, table, smart)
        else:
            turn_on(x1,x2,y1,y2, table, smart)
