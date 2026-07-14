class Solution:
    def binaryGap(self, n: int) -> int:
        maxval = 0
        values = bin(n)[2:]
        left, right = 0, len(values)-1

        # eliminate zeros around the values
        while values[left] == 0:
            left += 1
        while values[right] == 0:
            right -= 1
        
        left += 1 # skip 1st 1 of the window

        count = 0
        while left <= right:
            count += 1
            if values[left] == '1':
                maxval = max(maxval, count)
                count = 0
            left += 1
        
        return maxval
