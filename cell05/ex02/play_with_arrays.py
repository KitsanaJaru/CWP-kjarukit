nums = [2, 8, 9, 48, 8, 22, -12, 2]
print(nums)

for i in range(len(nums) - 1, -1, -1):
    nums[i] += 2
    if nums[i] < 5:
        del nums[i]

print(nums)