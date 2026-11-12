class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        data = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        count = 0

        for char in text:
            if char in data:
                data[char] += 1
                if data['l'] >= 2 and data['o'] >= 2 and data['b'] >= 1 and data['a'] >= 1 and data['n'] >= 1:
                    count += 1
                    data['l'] -= 2
                    data['o'] -= 2
                    data['b'] -= 1
                    data['a'] -= 1
                    data['n'] -= 1
        
        return count
