class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def binsearch(rowidx, start, end): # O(log cols)
            if start > end:
                return False
            mid = (start + end) >> 1
            ele = matrix[rowidx][mid]
            if ele == target:
                return True
            if ele > target:
                return binsearch(rowidx, start, mid-1)
            else:
                return binsearch(rowidx, mid+1, end)

        for row in range(rows): # O(rows) + O(log n) = O(rows log cols)
            if matrix[row][0] <= target and binsearch(row, 0, cols-1): # O(log cols)
                return True
        
        return False

# Time: O(rows * log(cols))
# Space: O(log(cols))   # recursion call stack