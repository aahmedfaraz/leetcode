class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(prev, remaining):
            if not remaining:
                return [prev] # array of arrays
            perms = []
            for i in range(len(remaining)):
                perms.extend(dfs(prev + [remaining[i]], remaining[:i] + remaining[i+1:]))
            return perms
        return dfs([], nums)

# Time = O(n!), factorial
# Space = O(n!), factorial