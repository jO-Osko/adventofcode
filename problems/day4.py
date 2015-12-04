DAY = 4


from hashlib import md5


def part1(inpu):
    a = 0
    while not md5( (inpu + str(a)).encode("utf-8")).hexdigest().startswith("00000"):
        a += 1
    return a
    

def part2(inpu):
    a = 0
    while not md5( (inpu + str(a)).encode("utf-8")).hexdigest().startswith("000000"):
        a += 1
    return a
    
