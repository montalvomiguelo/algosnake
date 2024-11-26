def robotWithString(s):
    def minChar():
        for i in range(26):
            if counts[i]:
                return chr(i + ord("a"))

        return "a"

    counts = [0] * 26
    for c in s:
        counts[ord(c) - ord("a")] += 1

    t = []
    p = []
    for c in s:
        t.append(c)
        counts[ord(c) - ord("a")] -= 1

        while t and t[-1] <= minChar():
            p.append(t.pop())

    while t:
        p.append(t.pop())

    return "".join(p)


print(robotWithString("bydizfve"))
