def isPathCrossing(path):
    curr = (0, 0)
    seen = set([curr])
    directions = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    for move in path:
        x, y = curr
        dx, dy = directions[move]
        next = (dx + x, dy + y)

        if next in seen:
            return True

        curr = next
        seen.add(curr)

    return False


print(isPathCrossing("NESWW"))
