def distributeCookies(cookies, k):
    def backtrack(curr, i, remain):
        if n - i < remain:
            return float("inf")

        if i == n:
            return max(curr)

        ans = float("inf")
        for j in range(k):
            remain -= int(curr[j] == 0)
            curr[j] += cookies[i]
            ans = min(ans, backtrack(curr, i + 1, remain))
            curr[j] -= cookies[i]
            remain += int(curr[j] == 0)

        return ans

    n = len(cookies)
    return backtrack([0] * k, 0, k)


print(distributeCookies([8, 15, 10], 2))
