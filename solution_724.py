def pivotIndex(nums):
    sumLeft = 0
    sumRight = sum(nums)

    for i in range(len(nums)):
        num = nums[i]
        sumRight -= num
        if sumRight == sumLeft:
            return i

        sumLeft += num

    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
