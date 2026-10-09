
import heapq

class Solution:
    def isPossible(self, target: list[int]) -> bool:
        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:
            largest = -heapq.heappop(max_heap)
            rest = total - largest

            if largest == 1 or rest == 1:
                return True

            if rest == 0 or largest <= rest:
                return False

            prev = largest % rest

            if prev == 0:
                return False

            total = rest + prev
            heapq.heappush(max_heap, -prev)
