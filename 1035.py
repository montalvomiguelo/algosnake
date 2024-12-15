def maxUncrossedLines(nums1, nums2):
    def dp(i, j):
        if i == len(nums1) or j == len(nums2):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if nums1[i] == nums2[j]:
            memo[(i, j)] = 1 + dp(i + 1, j + 1)
        else:
            memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))

        return memo[(i, j)]

    memo = {}
    return dp(0, 0)

print(maxUncrossedLines([1, 4, 2], [1, 2, 4]))
