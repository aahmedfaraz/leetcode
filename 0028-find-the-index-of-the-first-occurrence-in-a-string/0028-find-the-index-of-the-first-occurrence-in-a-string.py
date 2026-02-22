class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        #            0 1 2 3 4 5 6 7 8
        # haystack = s a d b u t s a d = 9

        #          0 1 2
        # needle = s a d = 3

        def checkWindow(ind: int) -> bool:
            if (ind + m) > n: return False
            k = 0
            for i in range(ind, ind + m):
                if haystack[i] != needle[k]: return False
                k += 1
            return True

        for i in range(n):
            if haystack[i] == needle[0] and checkWindow(i):
                return i
        
        return -1