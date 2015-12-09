DAY = 9

from collections import defaultdict as dd
from functools import lru_cache

def solve(data, minimize=True):
    graph = dd(dict)
    for line in data:
        fro, mix, to, _, cost = line.split()
        cost = int(cost)
        graph[fro][to] =cost
        graph[to][fro] = cost
    cities = list(graph.keys())

    @lru_cache(maxsize=None)
    def shortest_path(current, visited, to_go):
        if to_go == 0:
            return 0
        rtr = float("inf") if minimize else float("-inf")
        for j in range(len(cities)):
            if not visited[j] and cities[j] in graph[current]:
                _visited = list(visited)
                _visited[j] = 1
                if minimize:
                    rtr = min(rtr, shortest_path(cities[j], tuple(_visited), to_go-1) + graph[current][cities[j]])
                else:
                    rtr = max(rtr, shortest_path(cities[j], tuple(_visited), to_go-1) + graph[current][cities[j]])
        return rtr

    paths = {cities[j]: shortest_path(cities[j], tuple([0 if j != i else 1 for i in range(len(cities))]), to_go=len(cities)-1) for j in range(len(cities))}
    if minimize:
        return min(paths.values())
    return max(paths.values())


def part1(data):
    return solve(data.split("\n"))

def part2(data):
    return solve(data.split("\n"), False)


TEST = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

DATA = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

print(part1(DATA))
print(part2(DATA))
