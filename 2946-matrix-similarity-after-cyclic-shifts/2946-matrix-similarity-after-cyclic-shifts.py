import copy
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        k %= cols

        new = []

        for row in range(rows):
            new.append(mat[row][k:] + mat[row][:k])

        return new == mat