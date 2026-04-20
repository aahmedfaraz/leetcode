class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [(['.']*n) for _ in range(n)]
        valids = []
        res = []

        def dfs(board, queens):
            nonlocal res
            # If all queens are filled
            if len(queens) == n:
                print(board)
                res.append([''.join(row[:]) for row in board])
                return
            
            # Fill new queen
            row = len(queens)
            for col in range(n): # try all possible ways for new queen
                position_is_safe = True
                # check if this position is fine
                for queen in queens:
                    qr, qc = queen[0], queen[1]
                    if qr == row or qc == col or (row+col) == (qr+qc) or (row-col) == (qr-qc):
                        position_is_safe = False
                        break
                if position_is_safe:
                    # add new values
                    board[row][col] = 'Q'
                    queens.add((row, col))

                    # runs dfs
                    dfs(board, queens)

                    # reset values
                    board[row][col] = '.'
                    queens.remove((row, col))
        
        dfs(board, set())

        return res