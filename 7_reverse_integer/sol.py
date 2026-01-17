class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        # Convert int to string
        int_str = str(x)

        # Reverse it
        reversed_int = 0
        if x < 0:
            int_str = int_str[1:]
            reversed_int = -int(int_str[::-1])
        else:
            reversed_int = int(int_str[::-1])

        # Check limit
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        # Return
        return reversed_int

# Example usage
print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(1534236469))

# Time complexity: O(log10(n)) where n is the absolute value of x
# Space complexity: O(1)

# OUTPUT:
# 321
# -321
# 0