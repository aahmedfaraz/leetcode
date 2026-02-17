class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # space complexity = 4^n
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

        combs = [""]

        for num in digits: # can run upto 4 times since digits length <= 4
            new_arr = []
            alphabets = data[num] # ['d', 'e', 'f']
            for prev_comb in combs: # prev_comb = 'a' then 'b' then 'c' - can run upto 4^n times
                for char in alphabets: # char = 'd' then 'e' then 'f' - can run upto 4 times
                    new_arr.append(prev_comb + char)
            combs = new_arr

        return combs
        
# Time complexity = 4^n, where n can be max 4 so, 4^4, which is constant due to constraints
# Space complexity = 4^n, where n is 8 numbers on phone so, 4^7, which is constant again