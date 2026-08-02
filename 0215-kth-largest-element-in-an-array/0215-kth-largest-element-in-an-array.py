import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # fill heap
        maxheap = []
        for num in nums: # O(n) + O(log n) = O(n log n)
            heapq.heappush(maxheap, -num) # O(log n) due to heapify up
        
        # get kth max element
        for i in range(k): # O(k) + O(log n) = O(k log n)
            if i == k-1:
                return -heapq.heappop(maxheap) # O(log n)
            else:
                heapq.heappop(maxheap)

# Time = O(n log n) + O(k log n) = O((n+k) log n) = O(n log n)
# Space = O(n). Heap stores all n elements