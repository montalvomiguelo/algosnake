from functools import cache


def generate(numRows):
    @cache
    def dp(i):
        if i == 1:
            return [[1]]

        ans = dp(i - 1)
        row = [1] * i
        for i in range(1, i - 1):
            prevRow = ans[-1]
            row[i] = prevRow[i - 1] + prevRow[i]

        ans.append(row)
        return ans

    return dp(numRows)


print(generate(5))
