class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # mark all border boxes to T
        def fillT(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return
            board[row][col] = 'T'
            fillT(row+1, col)
            fillT(row-1, col)
            fillT(row, col+1)
            fillT(row, col-1)

        for col in range(cols):
            # first row
            if board[0][col] == 'O':
                fillT(0, col)
            # last row
            if board[rows-1][col] == 'O':
                fillT(rows-1, col)

        for row in range(rows):
            # first col
            if board[row][0] == 'O':
                fillT(row, 0)
            # last col
            if board[row][cols-1] == 'O':
                fillT(row, cols-1)

        # turn everything else to 'X' and 'T' to 'O'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'