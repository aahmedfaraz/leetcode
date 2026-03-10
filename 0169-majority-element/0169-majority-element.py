class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        maxcount = 0
        maxval = 0
        curr = nums[0]
        count = 0
        for num in nums:
            if num == curr:
                count += 1
            else:
                if count >= maxcount:
                    maxcount = count
                    maxval = curr
                curr = num
                count = 1
        if count > maxcount:
            return curr
        return maxval