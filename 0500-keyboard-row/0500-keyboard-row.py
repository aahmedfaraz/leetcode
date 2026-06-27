class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr = set(list("qwertyuiop"))
        sr = set(list("asdfghjkl"))
        tr = set(list("zxcvbnm"))

        res = []

        for word in words:
            xword = word.lower()
            mismatch = False
            # check fr
            for ch in xword:
                if ch not in fr:
                    mismatch = True
                    break
            if not mismatch:
                res.append(word)
                continue

            mismatch = False
            # check sr
            for ch in xword:
                if ch not in sr:
                    mismatch = True
                    break
            if not mismatch:
                res.append(word)
                continue

            mismatch = False
            # check tr
            for ch in xword:
                if ch not in tr:
                    mismatch = True
                    break
            if not mismatch:
                res.append(word)
                continue
        
        return res