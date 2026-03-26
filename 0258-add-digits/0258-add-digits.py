class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(list(map(int, list(str(num)))))
        return num