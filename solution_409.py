from collections import Counter


def longestPalindrome(s):
    freq = Counter(s)
    hasOddFreq = False
    ans = 0

    for val in freq.values():
        if val % 2 == 0:
            ans += val
        else:
            ans += val - 1
            hasOddFreq = True

    if hasOddFreq:
        ans += 1

    return ans


print(longestPalindrome("abccccdd"))
