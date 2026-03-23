class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        lenN1, lenN2 = len(num1), len(num2)
        n1, n2 = 0, 0
        for i, n in enumerate(num1):
            n1 += (10**(lenN1-i-1)) * (ord(n) - 48)
        for i, n in enumerate(num2):
            n2 += (10**(lenN2-i-1)) * (ord(n) - 48)
        return str(n1 * n2)