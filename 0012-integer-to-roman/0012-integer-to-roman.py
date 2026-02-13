class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        i = 0
        rom = ""

        for i, symbol in enumerate(values):
            if num == 0: break

            if num >= values[symbol]:
                quan = num // values[symbol]
                rom += symbol * quan
                num %= values[symbol]
        
        return rom