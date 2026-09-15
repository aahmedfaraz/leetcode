class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * n
        judge = [1] * n

        for a, b in trust:
            a -= 1
            b -= 1
            judge[a] = 0
            trusts[b] += 1
        
        for person in range(n):
            if trusts[person] == (n-1) and judge[person] == 1:
                return person+1
        
        return -1