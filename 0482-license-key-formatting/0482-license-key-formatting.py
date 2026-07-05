class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        totalchrs = len(s) - s.count('-')
        if totalchrs == 0:
            return ""
        ans = totalchrs % k
        fg = k if ans == 0 else ans
        fgi = False
        res = ""
        og = k

        for ch in s:
            if ch != '-':
                if not fgi:
                    res += ch.upper()
                    fg -= 1
                    if fg == 0:
                        res += '-'
                        fgi = True
                else:
                    res += ch.upper()
                    og -= 1
                    if og == 0:
                        og = k
                        res += '-'
        
        return res[:-1] if res[-1] == '-' else res
