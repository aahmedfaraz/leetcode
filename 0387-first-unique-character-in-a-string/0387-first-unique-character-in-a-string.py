class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for chr in s:
            if chr in counter:
                counter[chr] += 1
            else:
                counter[chr] = 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        
        return -1