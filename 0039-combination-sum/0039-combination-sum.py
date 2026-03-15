class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(prev, prevSum, remaining):
            nonlocal combinations
            if prevSum == target:
                combinations.append(prev)

            if not remaining or prevSum > target:
                return
            
            for i, num in enumerate(remaining):
                dfs(prev+[num], prevSum + num, remaining[i:])
        
        dfs([], 0, candidates)
        
        return combinations                