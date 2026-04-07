class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while True:
            if n == 1:
                return True
            
            if n in visited:  # found loop
                return False
            
            visited.add(n)
            
            res = 0
            for digit in str(n):
                res += int(digit) ** 2
            
            n = res