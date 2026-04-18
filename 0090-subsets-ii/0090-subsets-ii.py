class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def dfs(prev, remaining):
            nonlocal res
            res.add(tuple(prev))
            if not remaining:
                return
            
            for i in range(len(remaining)):
                dfs(prev + [remaining[i]], remaining[i+1:])
        
        dfs([], nums)

        return list(map(list, res))