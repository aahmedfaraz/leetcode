class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in s.split(" "): # O(words)
            res.append(word[::-1]) # O(1)
        return " ".join(res) # O(words)
# Time = O(words) = O(n)
# Space = O(n)