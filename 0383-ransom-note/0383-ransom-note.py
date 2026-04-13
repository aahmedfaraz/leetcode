from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(magazine)
        b = Counter(ransomNote)
        return len(a-b) >= 0 and len(b-a) <= 0