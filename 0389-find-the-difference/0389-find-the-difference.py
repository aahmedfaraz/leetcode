class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        data = {}
        for char in s:
            if char not in data:
                data[char] = 1
            else:
                data[char] += 1

        for char in t:
            if char not in data or data[char] == 0:
                return char
            elif data[char]:
                data[char] -= 1
        
        return ""