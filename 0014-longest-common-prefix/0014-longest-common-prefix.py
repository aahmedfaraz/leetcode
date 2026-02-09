class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for i in range(len(strs)-1):
            a = strs[i]
            b = strs[i+1]
            curr = ""
            j = 0
            while j < len(a) and j < len(b) and a[j] == b[j]:
                curr += a[j]
                j += 1
            if len(curr) < len(longest):
                longest = curr
        return longest