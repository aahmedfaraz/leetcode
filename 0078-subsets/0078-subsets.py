class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [[], ['A'], ['B'], ['A', 'B'], ['C'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'C']]
        # [[], [1],   [2],    [1,2],     [3],   [ 1,3],      [2,3],      [1,2,3]]

        subsets = [[]]
        
        # subsets = [ [] ]
        
        # Iteration 1 - 'A' from ['A', 'B', 'C'] - outer
        # new_subsets = []
        # Iteration 1 - 

        for num in nums:
            new_subsets = []    
            for subset in subsets:
                new_subsets.append(subset + [num])      
            subsets = subsets + new_subsets

        return subsets
        
        # 2^N
        # EXPONENTIAL 