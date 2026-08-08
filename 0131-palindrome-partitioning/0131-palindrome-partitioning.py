class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [([False] * n) for _ in range(n)]

        for i in range(n):
            row, col = 0, i
            while col < n:
                # Base Case
                if row == col:
                    dp[row][col] = True
                else: # Fill DP
                    if col - row <= 2:
                        dp[row][col] = s[row] == s[col]
                    else:
                        dp[row][col] = s[row] == s[col] and dp[row+1][col-1]
                row += 1
                col += 1

        res = []
        
        def partition(subs, start):
            nonlocal res
            if start == n:
                res.append(subs.copy())
            else:
                for cut in range(start+1, n+1):
                    if dp[start][cut-1]: # is palindrome
                        subs.append(s[start:cut])
                        partition(subs, cut)
                        subs.pop()

        partition([], 0)

        return res
