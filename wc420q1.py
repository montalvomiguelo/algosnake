def stringSequence(target):
    ans = []
    curr = []
    for letter in target:
        curr.append("a")
        ans.append("".join(curr[:]))
        if letter == curr[-1]:
            continue
        else:
            while letter != curr[-1]:
                curr[-1] = chr(ord(curr[-1]) + 1)
                ans.append("".join(curr[:]))

    return ans

print(stringSequence("he"))
