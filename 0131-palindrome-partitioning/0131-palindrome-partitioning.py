class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return []
        if len(s) == 1: return [[s]]

        paliset = set()

        def isPali(subs: str) -> bool:
            left, right = 0, len(subs)-1
            while left < right:
                if subs[left] != subs[right]:
                    return False
                left += 1
                right -= 1
            return True

        def fillPaliSet(subs: str):
            for start in range(len(subs)):
                for cut in range(start+1, len(subs)+1):
                    if isPali(subs[start: cut]):
                        paliset.add((start, cut))

        fillPaliSet(s)
        # print(paliset)

        res = []

        def dfs(path, start, end):
            # print(path, start, end)
            if start == end:
                res.append(path.copy())
                return

            for cut in range(start+1, end+1):
                if (start, cut) in paliset:
                    path.append(s[start: cut])
                    dfs(path, cut, end)
                    path.pop()

        dfs([], 0, len(s))

        # print(res)

        return res
            
# Time = 
# Space = 