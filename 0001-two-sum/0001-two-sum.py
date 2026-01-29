class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0, 1]
        seen = {}
        for i, num in enumerate(nums): # O(n)
            diff = target - num
            if diff in seen:
                return [seen[diff], i] # O(1)
            else:
                seen[num] = i # O(1)
        return [-1, -1]

# Time complexity = O(n)
# Space complexity = O(n), we are storing in seen dictionary