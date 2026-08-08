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
                    if s[row] == s[col]:
                        midx, midy = row+1, col-1
                        if midx == midy or midy < midx:
                            dp[row][col] = True
                        else:
                            dp[row][col] = dp[midx][midy]
                    else:
                        dp[row][col] = False
                row += 1
                col += 1

        res = []
        
        def partition(cuts, start):
            nonlocal res
            if start == n:
                prev = 0
                partitions = []
                for i in range(len(cuts)):
                    partitions.append(s[cuts[i-1] if (i-1) > -1 else 0: cuts[i]])
                res.append(partitions)
            else:
                for cut in range(start+1, n+1):
                    if dp[start][cut-1]: # is palindrome
                        cuts.append(cut)
                        partition(cuts, cut)
                        cuts.pop()

        partition([], 0)

        return res
