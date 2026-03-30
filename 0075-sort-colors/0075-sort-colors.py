class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j = 0, len(nums)-1

        while nums[i] == 0 and i < j:
            i += 1
        while nums[j] == 2 and i < j:
            j -= 1

        k = i

        while k <= j:
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                while nums[i] == 0 and i < j:
                    i += 1
                if nums[k] == 2:
                    nums[k], nums[j] = nums[j], nums[k]
                    while nums[j] == 2 and i < j:
                        j -= 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                while nums[j] == 2 and i < j:
                    j -= 1
                if nums[k] == 0:
                    nums[k], nums[i] = nums[i], nums[k]
                    while nums[i] == 0 and i < j:
                        i += 1
            if i > k:
                k = i
            else:
                k += 1