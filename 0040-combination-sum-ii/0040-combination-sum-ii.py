class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()        
        res = []

        def dfs(i, prev, prevSum):
            if prevSum == target:
                res.append(prev.copy())
                return

            if prevSum > target or i == len(candidates):
                return

            # include i
            prev.append(candidates[i])
            dfs(i+1, prev, prevSum+candidates[i])

            # skip i
            prev.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, prev, prevSum)

        dfs(0, [], 0)

        return res