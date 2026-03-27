class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        end = 0
        jumps = 0
        reach = 0

        for i in range(len(nums)-1):
            reach = max(reach, i + nums[i])
            if i == end:
                jumps += 1
                end = reach
        
        return jumps

# Time = O(n)
# Space = O(1)