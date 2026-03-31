class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(n):
            prefix = 1 << i
            for num in reversed(res):
                res.append(prefix | num)
        
        return res