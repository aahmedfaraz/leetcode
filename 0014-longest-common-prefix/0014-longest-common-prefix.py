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

# time complexity
# - for loop = O(n)
#   - nested while = O(length of largest string in strs)
# Overall = O(n) * O(largest str len) = O(n * len of largest string)

# space complexity = O(1), only saving prefix