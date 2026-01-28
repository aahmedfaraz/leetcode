class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])

        # Build 2D prefix sum
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefix[r][c] = (
                    mat[r-1][c-1]
                    + prefix[r-1][c]
                    + prefix[r][c-1]
                    - prefix[r-1][c-1]
                )

        # Helper to check if square of size k exists
        def exists_square(k):
            for r in range(k, rows + 1):
                for c in range(k, cols + 1):
                    square_sum = (
                        prefix[r][c]
                        - prefix[r-k][c]
                        - prefix[r][c-k]
                        + prefix[r-k][c-k]
                    )
                    if square_sum <= threshold:
                        return True
            return False

        # Binary search on size
        left, right = 0, min(rows, cols)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if exists_square(mid):
                ans = mid
                left = mid + 1   # try bigger square
            else:
                right = mid - 1  # try smaller square

        return ans