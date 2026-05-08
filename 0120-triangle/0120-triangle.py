class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle)-1, 0, -1): # O(row)
            for col in range(len(triangle[row])-1): # O(col)
                triangle[row-1][col] += min(triangle[row][col], triangle[row][col+1])
        return triangle[0][0]

# Time = O(row x col) = O(n)
# Space = O(1)