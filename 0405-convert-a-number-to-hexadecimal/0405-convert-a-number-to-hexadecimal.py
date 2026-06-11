class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = []
        
        # treat number as 32-bit unsigned
        num &= 0xffffffff
        
        while num > 0:
            digit = num & 15  # last 4 bits
            result.append(hex_chars[digit])
            num >>= 4
        
        return "".join(reversed(result))