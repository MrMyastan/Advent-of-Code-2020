from typing import Tuple


with open("input.txt") as f:
    map = f.read()

map = map.splitlines()

def slope(rise: int, run: int):
    x = 0
    y = 0
    yield x, y
    while True:
        x += run
        y += rise
        yield x, y

max = len(map) - 1
width = len(map[0])
hits = 0
for x, y in slope(1, 3):
    if y > max:
        break
    if map[y][x % width] == "#":
        hits += 1

print(hits)