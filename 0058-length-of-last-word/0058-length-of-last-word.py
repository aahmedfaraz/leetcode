class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        while i >= 0:
            if s[i] == ' ': 
                if count == 0:
                    i -= 1
                    continue # ignore last spaces
                else:
                    return count
            if s[i] != ' ':
                count += 1
            i -= 1
        return count

# time complexity = O(n)
# space complexity = O(1)