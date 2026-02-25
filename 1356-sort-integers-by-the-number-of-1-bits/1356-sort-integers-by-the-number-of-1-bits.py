import heapq

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        heap = []
        for num in arr:
            total1s = bin(num).count('1')
            heapq.heappush(heap, (total1s, num))

        res = []
        while heap:
            _, num = heapq.heappop(heap)
            res.append(num)
        return res

# time complexity = O(n log n), filled heap in O(n), and got min val in O(log n)
# space complexity = O(n), using heap