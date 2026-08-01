class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0

        i, j, n = 0, 0, len(nums)
        csum, size = nums[0], float('inf')

        while i < n or j < n: # O(n)
            if csum >= target:
                size = min(size, j - i + 1)
                
            if csum < target:
                j += 1
                if j < n:
                    csum += nums[j]
                else:
                    return 0 if size == float('inf') else size
            else:
                if csum > 0:
                    csum -= nums[i]
                i += 1
            
            if i > j: j = i
            
            if csum >= target:
                size = min(size, j - i + 1)
        
        return 0 if size == float('inf') else size

# Time = O(n)
# Space = O(1)