def maxUncrossedLines(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]

print(maxUncrossedLines([1, 4, 2], [1, 2, 4]))
