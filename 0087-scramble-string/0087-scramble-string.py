from functools import cache
from collections import Counter
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        # stop if obvious or length is 1
        if Counter(s1) != Counter(s2): return False
        if s1 == s2: return True
        
        # split at random index
        for i in range(1, len(s1)):
            x = s1[:i]
            y = s1[i:]
            s2x = s2[:i]
            s2y = s2[i:]

            # randomly decide to swap
            if self.isScramble(x, s2x) and self.isScramble(y, s2y): # dont swap
                return True
            if self.isScramble(x, s2[len(y):]) and self.isScramble(y, s2[:len(y)]): # swap
                return True
        return False