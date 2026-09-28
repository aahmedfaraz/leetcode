class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        visited = set()

        res = []

        def genPerms(prev):
            nonlocal res

            if len(prev) == n:
                res.append(prev[:])
                return

            for num in nums:
                idx = len(prev)+1
                if num not in visited and (idx % num == 0 or num % idx == 0):
                    visited.add(num)
                    prev.append(num)
                    genPerms(prev)
                    prev.pop()
                    visited.remove(num)

        genPerms([])
        
        return len(res)