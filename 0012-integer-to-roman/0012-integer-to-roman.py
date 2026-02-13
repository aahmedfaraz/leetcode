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


        # while num > 0:
        #     if num >= values[symbols[i]]:
        #         quan = num // values[symbols[i]]
        #         rom += symbols[i] * quan
        #         num %= values[symbols[i]]
            
        #     print('before win check', rom)
        #     # check window of last 5 symbols
        #     if len(rom) >= 5:
        #         win = rom[-5:]
        #         if (win[0] != win[1]) and (win[1] == win[2] == win[3] == win[4]):
        #             rom = rom[:-5] + win[1] + symbols[i-3]
        #     print('after win check', rom)
        #     i += 1
        
        # print(rom, count)