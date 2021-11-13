with open("input.txt") as f:
    input = f.read()

nums = input.split("\n")
nums = list(map(int, nums))

for i in range(len(nums)):
    num = nums.pop()
    target = 2020 - num
    if target in nums:
        print(target * num)
        break