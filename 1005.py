import heapq


def largestSumAfterKNegations(nums, k):
    heapq.heapify(nums)
    while k > 0:
        heapq.heappush(nums, -heapq.heappop(nums))
        k -= 1

    return sum(nums)


print(largestSumAfterKNegations([3, -1, 0, 2], 3))
