def maxDistance(nums1, nums2):
    def binarySearch(target):
        left = 0
        right = len(nums2) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums2[mid] < target:
                right = mid - 1
            else:
                left = mid

        return left

    ans = 0
    for i in range(len(nums1)):
        j = binarySearch(nums1[i])

        if j > i:
            ans = max(ans, j - i)

    return ans


print(maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
