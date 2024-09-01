def reversePrefix(word, ch):
    left = 0
    ans = list(word)
    for right in range(len(word)):
        if word[right] != ch:
            continue

        while left < right:
            ans[left], ans[right] = (ans[right],
                                     ans[left])
            right -= 1
            left += 1

        return "".join(ans)

    return word


print(reversePrefix("abcdefd", "d"))
