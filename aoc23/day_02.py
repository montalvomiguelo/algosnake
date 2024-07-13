with open('day_02.txt') as f:
    lines = [l.strip('\n') for l in f]
    dic = {'red': 12, 'green': 13, 'blue': 14}
    ans = 0
    for l in lines:
        parts = l.split(': ')
        id = parts[0]
        sets = parts[1].split('; ')
        isValid = True
        for s in sets:
            cubes = s.split(', ')
            for c in cubes:
                count = int(c.split()[0])
                color = c.split()[1]
                if count > dic[color]:
                    isValid = False
                    break
        if isValid:
            ans += int(id[5:])

    print(ans)
