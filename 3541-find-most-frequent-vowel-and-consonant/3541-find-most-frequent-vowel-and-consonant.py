class Solution:
    def maxFreqSum(self, s: str) -> int:
        frequencies = [0 for _ in range(26)]

        for i in range(len(s)):
            letter = ord(s[i]) - ord('a') # character to index. 'a' means save at 0 index
            frequencies[letter] += 1

        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowel_freq = 0
        max_consonant_freq = 0

        for i in range(26):
            char = chr(i + ord('a')) # index to character. i=0 means 'a'
            if char in vowels:
                max_vowel_freq = max(max_vowel_freq, frequencies[i])
            else:
                max_consonant_freq = max(max_consonant_freq, frequencies[i])

        return max_vowel_freq + max_consonant_freq