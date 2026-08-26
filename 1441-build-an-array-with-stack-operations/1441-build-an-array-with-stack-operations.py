class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        num = 1
        ti = 0

        while ti < len(target):
            if num == target[ti]:
                res.append('Push')
                num += 1
                ti += 1
            else:
                while num != target[ti]:
                    res.append('Push')
                    res.append('Pop')
                    num += 1
            
        return res