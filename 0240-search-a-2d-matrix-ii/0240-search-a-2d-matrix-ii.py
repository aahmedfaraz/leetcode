class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def binsearch(rowidx, start, end): # O(log cols)
            while start <= end:
                mid = (start + end) >> 1
                ele = matrix[rowidx][mid]
                if ele == target:
                    return True
                if ele > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return False

        for row in range(rows): # O(rows) + O(log n) = O(rows log cols)
            if matrix[row][0] <= target and binsearch(row, 0, cols-1): # O(log cols)
                return True
        
        return False

# Time: O(rows * log(cols))
# Space: O(1) 