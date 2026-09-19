class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        comb, summ, combs = [], 0, []

        def dfs(k):
            nonlocal comb, summ, combs
            if summ > n:
                return

            if k == 0:
                if summ == n:
                    combs.append(comb[:])
                return
            
            start = 1
            if len(comb) > 0:
                start = comb[-1] + 1
            
            for i in range(start, 10):
                summ += i
                if summ <= n:
                    comb.append(i)
                    dfs(k-1)
                    comb.pop()
                summ -= i
            
        dfs(k)

        return combs