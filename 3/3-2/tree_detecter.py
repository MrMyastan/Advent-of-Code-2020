from typing import Tuple


with open("input.txt") as f:
    map = f.read()

map = map.splitlines()

def slope_points(rise: int, run: int):
    x = 0
    y = 0
    yield x, y
    while True:
        x += run
        y += rise
        yield x, y

def count_hits(map, rise, run):
    max = len(map) - 1
    width = len(map[0])
    hits = 0
    for x, y in slope_points(rise, run):
        if y > max:
            break
        if map[y][x % width] == "#":
            hits += 1
    return hits

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1

for slope in slopes:
    result *= count_hits(map, slope[1], slope[0])


print(result)