class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        curr = ""
        res = []

        for num in nums:
            curr += str(num)
            res.append(int(curr, 2) % 5 == 0)
        
        return res
