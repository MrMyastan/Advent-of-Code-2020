from typing import Optional, Tuple


with open("input.txt") as f:
    passes = f.read()

passes = passes.splitlines()

def binary_part(directions: str, low: str, high: str, u_bound: int) -> int:
    l_bound = 0
    for direction in directions:
        half_size = (u_bound - l_bound + 1) // 2
        if direction == low:
            u_bound -= half_size
        if direction == high:
            l_bound += half_size
    if l_bound == u_bound:
        return l_bound
    return -1

def calculate_seat(bp: str) -> Tuple[int, int]:
    return binary_part(bp[0:7], "F", "B", 127), binary_part(bp[7:], "L", "R", 7)

highest = 0
for bp in passes:
    row, col = calculate_seat(bp)
    id = (row * 8) + col
    if id > highest:
        highest = id

print(highest)
