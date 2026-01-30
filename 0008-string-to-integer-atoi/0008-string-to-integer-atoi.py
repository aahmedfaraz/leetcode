class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "": return 0

        size = len(s)
        i = 0
        num = 0

        # get rid of leading whitespaces
        while i < size and s[i] == " ":
            i += 1
        
        # determine sign
        sign = 1
        if i < size and s[i] in "+-":
            if s[i] == '-':
                sign = -1
            i +=1

        # skip leading zeros
        while i < size and s[i] == "0":
            i += 1
        
        # read numbers
        while i < size and s[i].isdigit():
            num = (num * 10) + (ord(s[i]) - ord("0"))
            i += 1
        
        MIN = -2**31
        MAX = 2**31 - 1
        num *= sign

        # apply limit and return
        return min(MAX, max(MIN, num))

# time complexity = O(n) since we will access all chars of s at most once
# space complexity = O(1) 