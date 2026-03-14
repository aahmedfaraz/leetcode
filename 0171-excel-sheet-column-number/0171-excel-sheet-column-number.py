class Solution:
    def titleToNumber(self, columnTitle: str) -> int:        
        res = 0
        for i in range(len(columnTitle)-1, -1, -1):
            index = len(columnTitle) - i - 1
            res += ((26**i) * (ord(columnTitle[index]) - ord('A') + 1))
        return res