def reverseOnlyLetters(s):
    def isLetter(l):
        code = ord(l)
        if code < 65 or (code > 90 and code < 97):
            return False

        return True

    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        if not isLetter(chars[left]):
            left += 1
            continue

        if not isLetter(chars[right]):
            right -= 1
            continue

        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


print(reverseOnlyLetters('Test1ng-Leet=code-Q!'))
