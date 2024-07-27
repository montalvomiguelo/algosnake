import heapq


class SeatManager:
    def __init__(self, n):
        self.heap = [i + 1 for i in range(n)]
        heapq.heapify(self.heap)

    def reserve(self):
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber):
        heapq.heappush(self.heap, seatNumber)


seatManager = SeatManager(5)
seatManager.reserve()
seatManager.reserve()
seatManager.unreserve(2)
seatManager.reserve()
seatManager.reserve()
seatManager.reserve()
seatManager.reserve()
seatManager.unreserve(5)
print(seatManager.heap)
