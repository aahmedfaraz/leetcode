from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        ct = Counter(t)
        win = s[l:r+1]
        cw = Counter(win)
        res = ""
        minl = float('inf')
        while r < len(s):
            win = s[l:r+1]
            if len(ct - cw) == 0: # current window has all t elements
                if len(win) < minl:
                    res = win
                    minl = len(win)
                cw[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < len(s):
                    if s[r] in cw:
                        cw[s[r]] += 1
                    else:
                        cw[s[r]] = 1
        return res