class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
# Time = O(n^2)
# Space = O(1)