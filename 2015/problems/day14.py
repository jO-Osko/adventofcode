DAY = 14

def part1(data, time=2503):
    return solve(data.split("\n"), time)

def solve(data, time):
    ma = 0
    for line in data:
        line = line.strip().split()
        speed, duration, rest = map(int, (line[3], line[6], line[-2]))
        normal = speed * (time// (duration+rest)) * duration
        last = speed * min(time % (duration+rest),duration)
        ma = max(ma, normal + last)
    return ma

def solve2(data, time):
    deers = []
    for line in data:
        line = line.strip().split()
        speed, duration, rest = map(int, (line[3], line[6], line[-2]))
        deers.append((speed, duration, rest))
    points = [0 for j in range(len(deers))]
    last_locations = [0 for j in range(len(deers))]
    for current_time in range(time):
        for i, (speed, duration, rest) in enumerate(deers):
            if current_time %  (duration + rest) < duration:
                last_locations[i] += speed
        m = max(last_locations)
        for i,l in enumerate(last_locations):
            if l == m:
                points[i] += 1

    return max(points)
        

def part2(data, time=2503):
    return solve2(data.split("\n"), time)


TEST = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


DATA = """Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds."""


print(part1(DATA))
print(part2(DATA))
