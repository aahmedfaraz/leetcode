class Solution:
    def isPalindrome(self, s: str) -> bool:
        def returnAscii(char):
            asc = ord(char)
            if asc >= 97 and asc <= 122: return asc
            if asc >=65 and asc <= 90: return asc + 32
            if asc >=48 and asc <= 57: return asc + 32
            return -1

        if len(s) == 1: return True
            
        i, j = 0, len(s)-1

        while i < j:
            iasc = returnAscii(s[i])
            if iasc == -1:
                i += 1
                continue
            jasc = returnAscii(s[j])
            if jasc == -1:
                j -= 1
                continue
            if iasc != jasc:
                return False
            i += 1
            j -= 1
        return True
