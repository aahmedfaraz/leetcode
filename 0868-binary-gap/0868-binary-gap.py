class Solution:
    def binaryGap(self, n: int) -> int:
        count = 0
        larg = 0
        window = False
        binnum = bin(n)[2:]
        for ch in binnum:
            if ch == '1':
                if window:
                    count += 1
                    larg = max(larg, count)
                    count = 0
                else:
                    window = True
            else:
                if window:
                    count += 1
        return larg
