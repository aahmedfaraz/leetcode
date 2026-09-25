class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        
        def bt(prev, i):
            nonlocal res

            prev.append(nums[i])

            if len(prev) > 1:
                res.add(tuple(prev[::]))
            
            for j in range(i+1, n):
                if nums[j] >= nums[i]:
                    bt(prev, j)
            
            prev.pop()
        
        for i in range(n):
            bt([], i)

        return [list(val) for val in res]
