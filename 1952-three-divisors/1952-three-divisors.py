class Solution:
    def isThree(self, n: int) -> bool:
        divs = 1

        for i in range(1, (n//2)+1):
            if n % i == 0:
                divs += 1
            if divs > 3:
                return False
        
        return divs == 3