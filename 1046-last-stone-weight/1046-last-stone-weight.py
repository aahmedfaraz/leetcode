import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-w for w in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            a = -heapq.heappop(maxheap)
            b = -heapq.heappop(maxheap)
            # print(maxheap, a, b)
            if a != b:
                heapq.heappush(maxheap, -abs(b-a))
        
        return -maxheap[0] if len(maxheap) else 0