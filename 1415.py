def happyString(n, k):
    def backtrack(curr):
        if len(curr) == n:
            ans.append(curr[:])
            return

        for letter in ["a", "b", "c"]:
            if not curr or letter != curr[-1]:
                curr.append(letter)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    if len(ans) < k:
        return ""

    return "".join(ans[k - 1])


print(happyString(1, 4))
