from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        odd_found = False

        for c in counts:
            if counts[c] % 2 == 0:
                length += counts[c]         # use all if even
            else:
                length += counts[c] - 1    # use the even part
                odd_found = True           # can place 1 odd in center

        if odd_found:
            length += 1                    # add 1 for center

        return length