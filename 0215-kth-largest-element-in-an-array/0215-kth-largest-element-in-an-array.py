import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # fill heap
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, -num)
        
        # get kth max element
        for i in range(k):
            if i == k-1:
                return -heapq.heappop(maxheap)
            else:
                heapq.heappop(maxheap)