class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        totalwords = len(words)
        res = []
        for i in range(totalwords):
            if words[i] == first and (i+1) < totalwords and words[i+1] == second and (i+2) < totalwords:
                res.append(words[i+2])
        return res