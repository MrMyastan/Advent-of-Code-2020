from typing import List
from field_validators import *

with open("input.txt") as f:
    batch = f.read()

required = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}

batch = batch.split("\n\n")

def flatten_pass(passport: str) -> List[str]:
    fields = []
    for line in passport.splitlines():
        for field in line.split(" "):
            fields.append(field)
    return fields

def verify_pass(passport: list) -> bool:
    if len(passport) < len(required):
        return False
    requirements_met = 0
    for field in passport:
        if field[0:3] in required and (required[field[0:3]](field[4:])):
            requirements_met += 1
    return requirements_met == len(required)

valid = 0
for passport in map(flatten_pass, batch):
    valid += verify_pass(passport)

print(valid)