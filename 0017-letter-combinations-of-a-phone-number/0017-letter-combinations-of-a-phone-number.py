class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        combs = data[digits[0]] # ['a', 'b', 'c']

        for i, num in enumerate(digits): # num = '2' to '9'
            if i == 0: continue
            new_arr = []
            alphabets = data[num] # ['d', 'e', 'f']
            for prev_comb in combs: # prev_comb = 'a' then 'b' then 'c'
                for char in alphabets: # char = 'd' then 'e' then 'f'
                    new_arr.append(prev_comb + char)
            combs = new_arr

        return combs