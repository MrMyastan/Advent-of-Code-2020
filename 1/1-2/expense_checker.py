from typing import Optional, Tuple

with open("input.txt") as f:
    input = f.read()

nums = input.split("\n")
nums = list(map(int, nums))

def find_combo(nums: list, sum: int) -> Optional[Tuple[int, int]]:
    for i in range(len(nums)):
        num = nums.pop()
        target = sum - num
        if target in nums:
            return (num, target)

for i in range(len(nums)):
    num = nums.pop()
    target = 2020 - num
    combo = find_combo(nums.copy(), target)
    if combo:
        print(num * combo[0] * combo[1])
        break