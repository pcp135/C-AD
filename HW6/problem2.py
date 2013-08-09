import heapq

class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)
    def push(self, value):
        heapq.heappush(self.heap, -value)
    def pop(self):
        return -heapq.heappop(self.heap)

