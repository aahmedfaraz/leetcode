class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        # match itself
        if mat == target: return True

        for _ in range(3): # rotate 90 clockwise 3 times to achieve all rotated positions
            # transpose
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            #  rev rows
            for row in range(n):
                for col in range(n//2):
                    mat[row][col], mat[row][n-col-1] = mat[row][n-col-1], mat[row][col]
            if mat == target: return True
        
        return False