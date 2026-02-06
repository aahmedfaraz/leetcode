class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        curr_con = 0
        for num in nums:
            if num == 0:
                max_con = max(max_con, curr_con)
                curr_con = 0
            else:
                curr_con += 1
        
        max_con = max(max_con, curr_con)
        return max_con