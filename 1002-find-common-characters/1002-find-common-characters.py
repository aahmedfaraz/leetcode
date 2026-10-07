class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words) < 2:
            return list(words[0])

        base = set(words[0])

        ans = []

        for ch in base:
            freq = min([word.count(ch) for word in words])
            ans.extend([ch] * freq)

        return ans