def combinationSum2(candidates, target):
    def backtrack(path, start, curr):
        if curr == target:
            ans.append(path[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if curr + candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(path, i + 1, curr + candidates[i])
            path.pop()

    ans = []
    candidates.sort()
    backtrack([], 0, 0)

    return ans


print(combinationSum2([5, 2, 1, 2], 5))
