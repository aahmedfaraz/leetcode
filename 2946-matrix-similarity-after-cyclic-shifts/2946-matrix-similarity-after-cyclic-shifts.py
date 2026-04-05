import copy
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if r % 2 == 0:  # left shift
                    if mat[r][c] != mat[r][(c + k) % cols]:
                        return False
                else:  # right shift
                    if mat[r][c] != mat[r][(c - k) % cols]:
                        return False
        return True

# Time = O(rows  x cols)
# Space = O(1)
