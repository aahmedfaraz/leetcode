class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        
        lps = ""

        for i in range(size): # O(n)
            # in case whole string is of same characters, no need to run loop on all characters
            if len(lps) == size:
                break
                
            # check palindrome of odd size
            curr_sq = s[i]
            left, right = i-1, i+1
            while left >= 0 and right <= (size-1) and s[left] == s[right]: # O(n)
                curr_sq = s[left] + curr_sq + s[right]
                left -= 1
                right += 1
            if len(curr_sq) > len(lps):
                lps = curr_sq
            
            # check palindrome of even size
            if i < (size-1) and s[i] == s[i+1]:
                curr_sq = s[i:i+2]
                left, right = i-1, i+2
                while left >= 0 and right <= (size-1) and s[left] == s[right]: # O(n)
                    curr_sq = s[left] + curr_sq + s[right]
                    left -= 1
                    right += 1
                if len(curr_sq) > len(lps):
                    lps = curr_sq

        return lps if len(lps) > 0 else s[0]

# Time complexity = O(n) * {O(n) + O(n)} = O(n) + O(n) = O(n^2)
# Space complexity = O(n) - using lps to store string