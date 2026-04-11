from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern): return False

        patternmem = defaultdict(tuple)
        wordsmem = defaultdict()
        for i in range(len(s)):
            val = tuple(s[i])
            patternmapat, wordmapat = None, None
            if pattern[i] in patternmem:
                patternmapat = patternmem[pattern[i]]
            if val in wordsmem:
                wordmapat = wordsmem[val]
            
            if not patternmapat and not wordmapat:
                patternmem[pattern[i]] = val
                wordsmem[val] = pattern[i]
            elif patternmapat and wordmapat and patternmapat == val and wordmapat == pattern[i]:
                continue
            else:
                return False
        return True