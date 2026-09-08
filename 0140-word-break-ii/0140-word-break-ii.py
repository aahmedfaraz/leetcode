class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        maxw = 0
        for word in wordDict:
            maxw = max(maxw, len(word))
        words = set(wordDict)

        res = []
        currcomb = []

        def dfs(i):
            nonlocal currcomb, res
            if i == n:
                res.append(" ".join(currcomb))
                return
            for j in range(i, n):
                if s[i:j+1] in words:
                    currcomb.append(s[i:j+1])
                    dfs(j+1)
                    currcomb.pop()
        dfs(0)

        return res