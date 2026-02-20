class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        left, right = 1, x // 2

        # x = 82

        while left <= right:
            mid = (left + right) // 2

            res = mid * mid
            if res <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

# time complexity: O(log n) -> x = 1,000,000 -> 20
# space complexity: O(1)







#         if x < 2: return x

#         # 82 -> 9

#         # 1 * 1 = 1
#         # 2 * 2 = 4
#         # 3 * 3 = 9
#         # 4 * 4 = 16
#         # 5 * 5 = 25
#         # 6 * 6 = 
#         # 7 * 7
#         # 8 * 8
#         # 9 * 9 = 81
#         # 10 * 10 = 100

#         i = 1
#         while (i * i) <= x:
#             i += 1

#         return i - 1

# # time = O(/x)
# # 1,000,000 -> 1000