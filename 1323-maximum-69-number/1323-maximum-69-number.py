class Solution:
    def maximum69Number (self, num: int) -> int:
        st = str(num)
        add = 3 * (10**(len(st)-1))
        
        for i in range(len(st)):
            if st[i] == '6':
                num += add
                return num
            else:
                add //= 10
        
        return num
            