from typing import Tuple


with open("input.txt") as f:
    db = f.read()

db = db.splitlines()

def process_rule(entry: str) -> Tuple[int, int, str, str]:
    pieces = entry.split(" ")
    minmax = pieces[0].split("-")
    return (int(minmax[0]), int(minmax[1]), pieces[1][0], pieces[2])

db = list(map(process_rule, db))

valid = 0

for rule in db:
    if rule[0] <= rule[3].count(rule[2]) <= rule[1]:
        valid += 1

print(valid)