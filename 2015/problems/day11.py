DAY = 11

def part1(data):
    data = [ord(c) for c in data]
    while not is_valid(data):
        for j in range(len(data)-1, -1,-1):
            data[j] = data[j]+1
            if data[j] > ord("z"):
                data[j] = ord("a")
            else:
                break
    return "".join(chr(c) for c in data)


def part2(data):
    data = [ord(c) for c in data]
    for j in range(len(data)-1, -1,-1):
        data[j] = data[j]+1
        if data[j] > ord("z"):
            data[j] = ord("a")
        else:
            break
    while not is_valid(data):
        for j in range(len(data)-1, -1,-1):
            data[j] = data[j]+1
            if data[j] > ord("z"):
                data[j] = ord("a")
            else:
                break
    return "".join(chr(c) for c in data)

def is_valid(s):
    for j in range(len(s)-1):
        if s[j] == s[j+1]:
            last = s[j]
            break
    else:
        return False
    for j in range(len(s)-1):
        if s[j] == s[j+1] and s[j] != last:
            break
    else:
        return False
    if ord("i") in s or ord("o") in s or ord("l") in s:
        return False
    
    for j in range(len(s)-2):
        if s[j]== s[j+1]-1 and s[j] == s[j+2]-2:
            break
    else:
        return False
    return True

p1 = part1("vzbxkghb")
print(p1)
print(part2(p1))
