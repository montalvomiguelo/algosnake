import heapq


def matchPlayersAndTrainers(players, trainers):
    players.sort()
    heapq.heapify(trainers)

    ans = 0
    for player in players:
        if not trainers:
            break
        trainer = heapq.heappop(trainers)
        while player > trainer and trainers:
            trainer = heapq.heappop(trainers)

        if player <= trainer:
            ans += 1

    return ans
