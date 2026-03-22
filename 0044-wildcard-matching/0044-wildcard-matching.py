class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # match empty string with empty pattern
        dp[0][0] = True

        # match p with empty string
        for i in range(1, m+1):
            dp[0][i] = dp[0][i-1] if p[i-1] == '*' else False

        # match p with s
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        
        return dp[n][m]

# Time = O(n x m)
# Space = O(n x m), DP Matrix