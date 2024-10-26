import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.seen = set()
        self.curr = 1

    def popSmallest(self):
        if not self.heap:
            ret = self.curr
            self.curr += 1
            return ret

        ret = heapq.heappop(self.heap)
        self.seen.remove(ret)
        return ret

    def addBack(self, num):
        if (num >= self.curr or
            num in self.seen):
            return

        heapq.heappush(self.heap, num)
        self.seen.add(num)
