class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n in visited: # found loop
                return False
            if n == 1:
                return True
            visited.add(n)
            nums = list(str(n))
            res = 0
            for num in nums:
                res += int(num)**2
            n = res
