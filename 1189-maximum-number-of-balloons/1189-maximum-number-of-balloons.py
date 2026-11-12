from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min(counter['b'], counter['a'], counter['n'], counter['l'] // 2, counter['o'] // 2)