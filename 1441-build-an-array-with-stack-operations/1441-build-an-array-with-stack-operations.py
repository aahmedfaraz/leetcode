class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        for num in range(1, n+1):
            if i >= len(target):
                break
            res.append('Push')
            if target[i] == num:
                i += 1
            else:
                res.append('Pop')
        return res