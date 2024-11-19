import heapq


def matchPlayersAndTrainers(players, trainers):
    heapq.heapify(players)
    heapq.heapify(trainers)

    ans = 0
    while players:
        player = heapq.heappop(players)
        if not trainers:
            break
        trainer = heapq.heappop(trainers)
        while player > trainer and trainers:
            trainer = heapq.heappop(trainers)

        if player <= trainer:
            ans += 1

    return ans

# print(matchPlayersAndTrainers([1, 1000000000], [1000000000, 1]))
# print(matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))
# print(matchPlayersAndTrainers([1, 1, 1], [10]))
