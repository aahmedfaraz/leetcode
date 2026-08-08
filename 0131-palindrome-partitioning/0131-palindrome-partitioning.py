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

# Time =>
#    DP = O(n^2)
#    Recursion = O(2^n-1) * (slicing O(n) + subs copy O(n))  = O(2n.2^n-1)
# Overall Time Complexity = O(n^2 + n.2^n-1) = O(n.2^n)

# Space =>
#    DP = O(n^2)
#    Recursion = Depth O(n) + subs copy O(n) = O(n)
#    Result = 2^n-1 partitions, and each partition store n characters = O(n.2^n-1)
# Overall Space complexity = O(n^2 + n.2^n-1) = O(n.2^n) with output, O(n^2) without output