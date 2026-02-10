class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) < 3: return []

        nums.sort()

        INF = float('inf')
        closest_sum = 0
        min_diff = INF
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                # get sum and difference with target
                triplet_sum = nums[i] + nums[left] + nums[right]
                sum_diff = abs(triplet_sum - target)

                # save closest sum
                if sum_diff < min_diff:
                    min_diff = sum_diff
                    closest_sum = triplet_sum

                # Move pointers based on actual sum vs target
                if triplet_sum < target:
                    left += 1
                elif triplet_sum > target:
                    right -= 1
                else:
                    return target  # exact match, obviously this is the closest sum

        return closest_sum