DAY = 10

from itertools import groupby

def look_and_say(ma, num="3113322113"):
    while ma:
        yield num
        num = "".join(str(len(list(listt))) + n for n, listt in groupby(num))
        ma -= 1

def part1():
  for j in look_and_say(41):
    pass
  return(len(j))
  
def part2():
  for j in look_and_say(51):
    pass
  return(len(j))
