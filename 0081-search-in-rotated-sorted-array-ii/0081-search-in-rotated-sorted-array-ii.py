class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def helper(left, right):
            if left > right:
                return False

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                return helper(left + 1, right - 1)

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return helper(left, mid - 1)
                else:
                    return helper(mid + 1, right)

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    return helper(mid + 1, right)
                else:
                    return helper(left, mid - 1)

        return helper(0, len(nums) - 1)