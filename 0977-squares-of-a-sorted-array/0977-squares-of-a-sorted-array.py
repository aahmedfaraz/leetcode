class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = []

        # find mid
        mid = 0
        maxval = abs(nums[0])
        for i in range(n):
            mag = abs(nums[i])
            if mag < maxval:
                mid = i
                maxval = mag
        
        # expand from mid
        res.append(abs(nums[mid])**2)
        left, right = mid-1, mid+1

        while left >=0 and right < n:
            l, r = abs(nums[left]), abs(nums[right])
            
            if l < r:
                res.append(l**2)
                left -= 1
            else:
                res.append(r**2)
                right += 1
        
        if left >= 0:
            for i in range(left, -1, -1):
                res.append(abs(nums[i])**2)
        if right < n:
            for i in range(right, n):
                res.append(abs(nums[i])**2)
        
        return res