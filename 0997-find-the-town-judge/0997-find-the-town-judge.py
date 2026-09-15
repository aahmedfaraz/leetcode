class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        havetrust = {(person+1): set() for person in range(n)}
        trusts = {(person+1): set() for person in range(n)}

        for i in range(len(trust)):
            a, b = trust[i]
            havetrust[b].add(a)
            trusts[a].add(b)

        for person in havetrust:
            if len(havetrust[person]) == (n-1) and len(trusts[person]) == 0:
                return person
        
        return -1