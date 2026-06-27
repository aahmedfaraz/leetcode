class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        longest = 0

        for num in data:
            if num-1 not in data:
                count = 1
                num += 1
                while num in data:
                    count += 1
                    num += 1
                longest = max(longest, count)
        
        return longest