class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(i):
            # print('start', i)
            if i in memo: return memo[i]
            if i == (n-1): return 0
            if i >= n: return 0
            mincost = float('inf')
            for pos in range(i+1, i+nums[i]+1):
                if pos < n:
                    mincost = min(mincost, 1 + dfs(pos))
            memo[i] = mincost
            # print('solved', i, ', cost', memo[i])
            return mincost
        return dfs(0)