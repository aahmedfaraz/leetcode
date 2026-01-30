class Solution:
    def myAtoi(self, s: str) -> int:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        integer = ""
        found_num = False
        found_char = False
        found_sign = False
        for i in range(len(s)):
            if s[i] in nums:
                integer += s[i]
                found_num = True
            elif found_num or found_char:
                break
            elif s[i] == "-":
                if found_sign: break
                integer = '-'
                found_sign = True
            elif s[i] == "+":
                if found_sign: break
                found_char = True
            elif s[i] != " ":
                break
        
        int_size = len(integer)
        integer = 0 if int_size == 0 or (int_size == 1 and integer[0] == '-') else int(integer)
        MIN = -2147483648
        MAX =  2147483647

        return MAX if integer > MAX else (MIN if integer < MIN else integer)