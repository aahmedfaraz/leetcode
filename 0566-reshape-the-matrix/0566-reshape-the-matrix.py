class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        srows, scols = len(mat), len(mat[0])

        if (srows*scols) != (r*c):
            return mat
        
        res = [[0] * c for _ in range(r)]
        i, j = 0, 0

        for row in range(srows):
            for col in range(scols):
                res[i][j] = mat[row][col]
                j += 1
                if j == c:
                    i += 1
                    j = 0
        
        return res