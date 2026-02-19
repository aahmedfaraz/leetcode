class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []

        if n == 4:
            if (nums[0]+nums[1]+nums[2]+nums[3]) == target:
                return [nums]
            else:
                return []

        nums.sort()
        quads = set()

        for i in range(n-3):
            for j in range(i+1, n-2):
                k, l = j+1, n-1
                while k < l:
                    four_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if four_sum == target:
                        quads.add((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        k += 1
                    elif four_sum > target:
                        l -= 1
                    else:
                        k += 1
        return list(quads)