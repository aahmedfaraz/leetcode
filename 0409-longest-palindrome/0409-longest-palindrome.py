from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        odd_found = False

        for char in counts:
            if counts[char] % 2 == 0:
                length += counts[char]
            else:
                length += counts[char] - 1
                odd_found = True
        
        if odd_found:
            length += 1

        return length