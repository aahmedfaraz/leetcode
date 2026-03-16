class Solution:
    def countAndSay(self, n: int) -> str:
        encoding = "1"
        if n == 1: return encoding
        while n > 1:
            prev = encoding[0]
            new_encoding = ""
            count = 0
            for num in encoding:
                if num == prev:
                    count += 1
                else:
                    new_encoding += f'{count}{prev}'
                    prev = num
                    count = 1
            if count > 0:
                new_encoding += f'{count}{prev}'
            encoding = new_encoding
            n -= 1
        return encoding