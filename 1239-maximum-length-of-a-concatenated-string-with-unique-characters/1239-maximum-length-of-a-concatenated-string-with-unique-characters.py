class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n = len(arr)
        newarr = []
        maxval = 0

        for i in range(n):
            uniset = set(list(arr[i]))
            if len(arr[i]) == len(uniset):
                newarr.append(uniset)
                maxval = max(maxval, len(uniset))
        
        m = len(newarr)
        maxval = 0

        def dfs(i, curr):
            nonlocal maxval

            maxval = max(maxval, len(curr))
            
            for j in range(i, m):
                merge = curr | newarr[j]

                if len(merge) == (len(curr) + len(newarr[j])):
                    dfs(j+1, merge)

        dfs(0, set())
        
        return maxval