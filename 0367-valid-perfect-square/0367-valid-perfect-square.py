from math import log
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        while left <= right:
            mid = (left+right) // 2

            sqval = mid**2

            if sqval == num:
                return True
            elif sqval > num:
                right = mid-1
            else:
                left = mid+1
        return False