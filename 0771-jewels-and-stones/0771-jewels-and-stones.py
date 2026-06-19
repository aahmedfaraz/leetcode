class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jmap = set(list(jewels))
        res = 0

        for stone in stones:
            if stone in jmap:
                res += 1

        return res
        
