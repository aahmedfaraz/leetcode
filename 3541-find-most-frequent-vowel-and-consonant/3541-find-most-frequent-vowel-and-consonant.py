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

# time complexity = O(n)
# space complexity = max O(26) = O(1)