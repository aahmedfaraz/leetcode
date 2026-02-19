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

        # print(nums)

        for i in range(n-3):
            # print('i', i, nums[i])
            for j in range(i+1, n-2):
                # print('j', j, nums[j])
                k, l = j+1, n-1
                while k < l:
                    # print('k, l', k, l, nums[k], nums[l])
                    four_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    # print('4sum', four_sum)
                    if four_sum == target:
                        quads.add((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        k += 1
                    elif four_sum > target:
                        l -= 1
                    else:
                        k += 1
        return list(quads)


#  i        j     k  l
#  0    1   2  3  4  5
# [-4, -1, -1, 0, 1, 2]     target = -1, n=6, i=6-4=2, j=6-3=3

# sum = -4, -1, -1, 2 = -4
# sum = -4, -1, 0, 2 = -3
# sum = -4, -1, 1, 2 = -2
# sum = -4, -1, 0, 2 = -3
# sum = -4, -1, 1, 2 = -2