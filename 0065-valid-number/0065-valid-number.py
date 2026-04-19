class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if "inf" in s.lower() or "nan" in s.lower():
                return False
            else:
                float(s)
            return True
        except:
            return False