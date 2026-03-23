class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i, j, k = 0, n-1, 0

        # place i and j to correct positions
        while i < n and nums[i] == 0:
            i += 1
        while j > -1 and nums[j] == 2:
            j -= 1
        
        k = i
        
        # use k to traverse whole array and swap accordingly
        while i < j and k <= j:
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                while i < n and nums[i] == 0:
                    i += 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
                while j > -1 and nums[j] == 2:
                    j -= 1
                while i < n and nums[i] == 0:
                    i += 1
                k = i
            else:
                k += 1