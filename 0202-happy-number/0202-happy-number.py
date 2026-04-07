class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n == 1:
                return True
            if n in visited: # found loop
                return False
            visited.add(n)
            nums = list(str(n))
            res = 0
            for num in nums:
                res += int(num)**2
            n = res
# Time: O(log n)
# Space: O(1)