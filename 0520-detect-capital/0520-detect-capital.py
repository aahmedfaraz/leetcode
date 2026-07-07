class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        countu, countl = 0, 0
        for ch in word:
            if 65 <= ord(ch) <= 90:
                countu += 1
            else:
                countl += 1
        return countu == len(word) or countl == len(word) or (65 <= ord(word[0]) <= 90 and countl == len(word)-1)