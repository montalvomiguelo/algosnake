def maxVowels(s, k):
    curr = 0
    vowels = {"a", "e", "i", "o", "u"}

    for i in range(k):
        curr += int(s[i] in vowels)

    ans = curr
    for i in range(k, len(s)):
        curr += int(s[i] in vowels)
        curr -= int(s[i - k] in vowels)
        ans = max(ans, curr)

    return ans


print(maxVowels("leetcode", 3))
