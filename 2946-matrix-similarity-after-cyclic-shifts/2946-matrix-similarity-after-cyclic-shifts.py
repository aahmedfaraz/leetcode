import copy
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        k %= cols

        new = copy.deepcopy(mat)

        for i in range(k):
            for row in range(rows):
                removed = new[row].pop(0)
                new[row].append(removed)

        return new == mat