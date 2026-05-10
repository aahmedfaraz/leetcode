class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for num in nums:
            if num in mem:
                return True
            mem[num] = 1
        return False