class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for pos in range(len(nums)):
            if pos > max_reach:
                return False

            max_reach = max(max_reach, pos + nums[pos])
        
        return True