class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        zeros = '0' * (32 - len(binary))
        rev = binary[::-1] + zeros
        num = int(rev, 2)
        return num

# time complexity = O(b), b = number of bits
# space complexity = O(b), b = number of bits
