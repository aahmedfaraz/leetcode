class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(prev, remaining):
            nonlocal res
            if len(prev) == k:
                res.append(prev)
            
            for i, num in enumerate(remaining):
                dfs(prev + [num], remaining[i+1:])
        dfs([], [n for n in range(1, n+1)])
        return res