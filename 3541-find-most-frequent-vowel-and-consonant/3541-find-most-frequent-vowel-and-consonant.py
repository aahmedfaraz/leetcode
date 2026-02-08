from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        max_vowel_freq = max(
            freq['a'],
            freq['e'],
            freq['i'],
            freq['o'],
            freq['u']
        )
        max_consonants_freq = max(
            freq['b'],
            freq['c'],
            freq['d'],
            freq['f'],
            freq['g'],
            freq['h'],
            freq['j'],
            freq['k'],
            freq['l'],
            freq['m'],
            freq['n'],
            freq['p'],
            freq['q'],
            freq['r'],
            freq['s'],
            freq['t'],
            freq['v'],
            freq['w'],
            freq['x'],
            freq['y'],
            freq['z']
        )

        return max_vowel_freq + max_consonants_freq





#         frequencies = [0 for _ in range(26)]

#         for i in range(len(s)):
#             letter = ord(s[i]) - ord('a') # character to index. 'a' means save at 0 index
#             frequencies[letter] += 1

#         vowels = ['a', 'e', 'i', 'o', 'u']
#         max_vowel_freq = 0
#         max_consonant_freq = 0

#         for i in range(26):
#             char = chr(i + ord('a')) # index to character. i=0 means 'a'
#             if char in vowels:
#                 max_vowel_freq = max(max_vowel_freq, frequencies[i])
#             else:
#                 max_consonant_freq = max(max_consonant_freq, frequencies[i])

#         return max_vowel_freq + max_consonant_freq

# # time complexity
# # Frequencies loop = O(n)
# # Calculate Max Freq. = O(26) = O(1)
# # Overall = O(n) + O(26) = O(n)

# # space complexity
# # Array saving frequencies = O(26) = O(1)