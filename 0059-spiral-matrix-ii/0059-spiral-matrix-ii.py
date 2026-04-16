class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [([0] * n) for _ in range(n)]
        layers = (n // 2) + 1
        i = 1

        for l in range(layers):
            # mention current box ranges as per layer
            start, end = l, l+n-1

            # travel first row
            col = start
            while col <= end:
                mat[start][col] = i
                i += 1
                col += 1

            # travel last col
            row = start + 1
            while row <= (end-1):
                mat[row][end] = i
                i += 1
                row += 1
            
            if start != end:
                # travel last row - reversed
                col = end
                while col >= start:
                    mat[end][col] = i
                    i += 1
                    col -= 1
            
            # travel first col - reversed
            row = end-1
            while row >= (start+1):
                mat[row][start] = i
                i += 1
                row -= 1
            
            # update n for next smaller box
            n -= 2

        return mat

# Time = O(n^2)
# Space = O(n^2) and O(1) without Output space