class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        INF = float('-inf')

        while left <= right:
            mid = (left + right) >> 1

            ln, rn = INF, INF
            
            if (mid-1) >= 0:
                ln = nums[mid-1]
            if (mid+1) <= n-1:
                rn = nums[mid+1]
            
            if ln < nums[mid] > rn:
                return mid
            elif ln > nums[mid]:
                right = mid-1
            elif rn > nums[mid]:
                left = mid+1
        
        return -1