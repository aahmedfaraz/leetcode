class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP (Knuth Morris Pratt) algorithm

        # build LPS (Longest Prefix Suffix)
        def generateLps(pattern: str) -> List[int]:
            n = len(needle)
            lps = [0] * n
            i, j = 0, 1

            while j < n:
                # print(i, j)
                if pattern[i] == pattern[j]:
                    i += 1
                    lps[j] = i
                    j +=1 
                else:
                    if i == 0:
                        j += 1
                    else:
                        i = lps[i-1]
            return lps

        lps = generateLps(needle)

        # KMP search

        m = len(haystack)
        n = len(needle)

        i, j = 0, 0

        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return i - j
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        
        return -1










#         # NAIVE APPROACH

#         n = len(haystack)
#         m = len(needle)

#         def checkWindow(ind: int) -> bool:
#             if (ind + m) > n: return False
#             k = 0
#             for i in range(ind, ind + m):
#                 if haystack[i] != needle[k]: return False
#                 k += 1
#             return True

#         for i in range(n):
#             if haystack[i] == needle[0] and checkWindow(i):
#                 return i
        
#         return -1

# # time complexity = O(m x n)
# # space complexity = O(1)