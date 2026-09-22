class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        o, c = 0, 0

        for ch in s:
            if ch.isalpha(): continue
            if ch == '(':
                o += 1
            else:
                if o > 0:
                    o -= 1
                else:
                    c += 1
        rem = o + c

        n = len(s)

        res = set()

        prev = []

        o, c = 0, 0

        maxval = float('-inf')

        def dfs(i):
            nonlocal rem, res, prev, o, c, maxval
            if c > o:
                return

            if i == n:
                if rem == 0 and o == c:
                    patt = "".join(prev)
                    if maxval < len(patt):
                        maxval = len(patt)
                        res = set()
                    res.add(patt)
                return
            
            if s[i].isalpha():
                prev.append(s[i])
                dfs(i+1)
                prev.pop()
            else:
                # Keep
                prev.append(s[i])
                o += (1 if s[i] == '(' else 0)
                c += (1 if s[i] == ')' else 0)
                dfs(i+1)
                o -= (1 if s[i] == '(' else 0)
                c -= (1 if s[i] == ')' else 0)
                prev.pop()

                # Remove
                if rem > 0:
                    rem -= 1
                    dfs(i+1)
                    rem += 1
        
        dfs(0)

        return list(res)
