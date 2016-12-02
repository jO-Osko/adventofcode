DAY = 20

def primes235(limit):
    yield 2; yield 3; yield 5
    if limit < 7: return
    modPrms = [7,11,13,17,19,23,29,31]
    gaps = [4,2,4,2,4,6,2,6,4,2,4,2,4,6,2,6] # 2 loops for overflow
    ndxs = [0,0,0,0,1,1,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,7]
    lmtbf = (limit + 23) // 30 * 8 - 1 # integral number of wheels rounded up
    lmtsqrt = (int(limit ** 0.5) - 7)
    lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30] # round down on the wheel
    buf = [True] * (lmtbf + 1)
    for i in range(lmtsqrt + 1):
        if buf[i]:
            ci = i & 7; p = 30 * (i >> 3) + modPrms[ci]
            s = p * p - 7; p8 = p << 3
            for j in range(8):
                c = s // 30 * 8 + ndxs[s % 30]
                buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]; ci += 1
    for i in range(lmtbf - 6 + (ndxs[(limit - 7) % 30])): # adjust for extras
        if buf[i]: yield (30 * (i >> 3) + modPrms[i & 7])


primes = list(primes235(10**7))

def part1(data):
    return smallest(int(data))

def part2(data, start=10):
    return smallest_with_limit(int(data), start)

def find_prime_divisors(num):
    for k in primes:
        n = 0
        while num % k == 0:
            n += 1
            num = num // k
        if n:
            yield(n, k)
        if num == 1:
            break
            
def presents(num):
    rtr = 1
    for power, prime in find_prime_divisors(num):
        rtr *= (prime**(power+1) - 1)//(prime -1)
    return rtr*10

def smallest(num):
    n = 10
    while 1:
        if presents(n) >= num:
            return n
        n += 1


def presents2(num):
    rtr = num
    for j in range(2,51):
        if num % j == 0:
            rtr += num//j
    return rtr*11
 
def smallest_with_limit(num, start_num=10):
    n = start_num
    while 1:
        if presents2(n) >= num:
            return n
        n += 1

DATA = "29000000"

start = part1(DATA)
print(start)
print(part2(DATA, start))
