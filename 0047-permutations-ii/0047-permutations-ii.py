class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # important for duplicate handling
        
        def dfs(prev, remaining):
            if not remaining:
                return [prev]
            
            permutations = []
            used = set()  # avoid duplicates at this level
            
            for i, num in enumerate(remaining):
                if num in used:
                    continue
                used.add(num)
                
                permutations.extend(
                    dfs(prev + [num], remaining[:i] + remaining[i+1:])
                )
            
            return permutations
        
        return dfs([], nums)