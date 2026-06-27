class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr = set(list("qwertyuiop"))
        sr = set(list("asdfghjkl"))
        tr = set(list("zxcvbnm"))

        res = []

        for word in words:
            cf = 0
            cs = 0
            ct = 0
            for ch in word:
                ch = ch.lower()
                if ch in fr:
                    cf += 1
                if ch in sr:
                    cs += 1
                if ch in tr:
                    ct += 1
            maxx = max(cf, max(cs, ct))
            if maxx == len(word):
                res.append(word)
        
        return res