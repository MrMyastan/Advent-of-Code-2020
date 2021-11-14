from typing import Tuple


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

calc_id = lambda row, col : (row * 8) + col

rows = {}
for bp in passes:
    row, col = calculate_seat(bp)
    if row not in rows:
        rows[row] = []
    rows[row].append(col)
    if len(rows[row]) == 8:
        del rows[row]

print(rows)

# from here i just did some mental logic im not entirely sure how to put into code
# (nor do i feel like putting into code)
# the results were:
# {1: [7, 6, 5], 88: [6, 5, 0, 4, 2, 7, 3], 102: [1, 4, 6, 5, 0, 3, 2]}
# i could see the lowest row works its way up in ids, and the highest goes up to a point
# both with no holes after/up to their start/end points
# so they were both full up
# leaving the only other empty row as 88
# and you can see the only seat not taken in 88 is 1
# so i used a calculator to do (88 * 8) + 1, then submitted
