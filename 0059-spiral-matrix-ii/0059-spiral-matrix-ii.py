class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def printmat(mat):
            for row in mat:
                print("\t".join(map(str, row)))
            print('-----------')

        mat = [([0] * n) for _ in range(n)]

        # printmat(mat)

        layers = (n // 2) + 1
        i = 1

        for l in range(layers):
            # print('LAYER', l)
            # mention current box ranges as per layer
            start, end = l, l+n-1

            # travel first row
            col = start
            while col <= end:
                mat[start][col] = i
                i += 1
                col += 1
            # printmat(mat)

            # travel last col
            row = start + 1
            while row <= (end-1):
                mat[row][end] = i
                i += 1
                row += 1
            # printmat(mat)
            
            if start != end:
                # travel last row - reversed
                col = end
                while col >= start:
                    mat[end][col] = i
                    i += 1
                    col -= 1
                # printmat(mat)
            
            # travel first col - reversed
            row = end-1
            while row >= (start+1):
                mat[row][start] = i
                i += 1
                row -= 1
            # printmat(mat)
            
            # update n for next smaller box
            n -= 2

        return mat