class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        j = 0

        def dfs(prev, rem):
            nonlocal res
            nonlocal j
            if res != "": return
            if not rem:
                j += 1
                if j == k:
                    res = "".join(map(str, prev))
                return
            for i, num in enumerate(rem):
                dfs(prev+[num], rem[:i]+rem[i+1:])
        
        dfs([], [num for num in range(1, n+1)])

        return res