class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) < 3: return []

        nums.sort()

        ans = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    left += 1

        return list(ans)

# Time complexity
# - Timsort = O(n log n)
# - For loop = O(n)
#   - Nested While loop = O(n)
#   - Set add = Amortized O(1), only O(n) if found rare hash conflict, so we consider O(1)
# Overall = O(nlogn) + {O(n) * O(n) * O(1)}
#         = O(nlogn) + O(n^2)
#         = O(n^2)
# Space complexity
# - ans set = O(n)