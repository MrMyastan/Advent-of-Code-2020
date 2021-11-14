from string import hexdigits

clr_dgs = hexdigits[0:16]

def byr(yr):
    return 1920 <= int(yr) <= 2002

def iyr(yr):
    return 2010 <= int(yr) <= 2020

def eyr(yr):
    return 2020 <= int(yr) <= 2030

def hgt(height):
    if len(height) == 5 and height[3:] == "cm":
        return 150 <= int(height[0:3]) <= 193
    elif len(height) == 4 and height[2:] == "in":
        return 59 <= int(height[0:2]) <= 76
    return False

def hcl(color):
    if len(color) != 7 and color[0] != "#":
        return False
    for char in color[1:]:
        if char not in clr_dgs:
            return False
    return True

def ecl(color):
    return color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def pid(passport_id):
    return len(passport_id) == 9