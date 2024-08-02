def reverseOnlyLetters(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        if not chars[left].isalpha():
            left += 1
            continue

        if not chars[right].isalpha():
            right -= 1
            continue

        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


print(reverseOnlyLetters('Test1ng-Leet=code-Q!'))
