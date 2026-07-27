class Solution:
    def isPali(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        que = [[[], s]]
        subs = []

        while que:
            prev, rem = que.pop()

            if not rem:
                subs.append(prev)
                continue

            for i in range(len(rem)): 
                part = rem[:i+1]
                if self.isPali(part):
                    que.append([prev+[part], rem[i+1:]])

        return subs
# Time = O(n * 2^n)
# Space = O(n^2)