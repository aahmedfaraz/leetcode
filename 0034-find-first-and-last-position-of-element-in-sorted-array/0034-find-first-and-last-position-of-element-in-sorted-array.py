class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def dncFirst():
            left, right, ans = 0, n-1, -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    right = mid - 1 # keep moving left
                else:
                    left = mid + 1
                if nums[mid] == target:
                    ans = mid
            return ans

        def dncLast():
            left, right, ans = 0, n-1, -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] <= target:
                    left = mid + 1 # keep moving right
                else:
                    right = mid - 1
                if nums[mid] == target:
                    ans = mid
            return ans
        
        return [dncFirst(), dncLast()]

# Time = O(log n) + O(log n) = O(log n)
# Space = O(1)