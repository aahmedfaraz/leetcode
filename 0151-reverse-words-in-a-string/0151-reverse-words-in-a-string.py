class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = []
        i = n-1

        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                end = i
                while i >= 0 and s[i] != ' ':
                    i -= 1
                res.append(s[i+1:end+1])

        return " ".join(res)