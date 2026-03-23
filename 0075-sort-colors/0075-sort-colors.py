class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i, j = 0, n - 1
        while i < n and nums[i] == 0:
            i += 1
        while j > -1 and nums[j] == 2:
            j -= 1
        
        while i < j:
            if nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                while j > -1 and nums[j] == 2:
                    j -= 1
                while i < n and nums[i] == 0:
                    i += 1
            elif nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                while i < n and nums[i] == 0:
                    i += 1
            else:
                k = i
                foundRequired = False
                while k <= j:
                    if nums[k] == 0:
                        foundRequired = True
                        nums[i], nums[k] = nums[k], nums[i]
                        i += 1
                        while i < n and nums[i] == 0:
                            i += 1
                    elif nums[k] == 2:
                        foundRequired = True
                        nums[j], nums[k] = nums[k], nums[j]
                        j -= 1
                        while j > -1 and nums[j] == 2:
                            j -= 1
                    k += 1
                if not foundRequired:
                    break