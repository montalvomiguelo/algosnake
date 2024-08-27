def moveZeroes(nums):
    left = 0
    right = 0
    n = len(nums)

    while left < n and right < n:
        if nums[left]:
            left += 1
            continue

        right = left + 1
        while right < n and not nums[right]:
            right += 1

        if right < n:
            nums[left], nums[right] = (
                nums[right], nums[left])

        left += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
