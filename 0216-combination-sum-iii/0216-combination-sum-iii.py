class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        combs = []

        def dfs(comb, summ, k):
            # print(comb, summ, k)
            nonlocal combs
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
                comb.append(i)
                k -= 1
                dfs(comb, summ, k)
                k += 1
                comb.pop()
                summ -= i
            
        dfs([], 0, k)

        return combs