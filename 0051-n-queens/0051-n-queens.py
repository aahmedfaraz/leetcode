class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(queens):
            nonlocal res
            # If all queens are filled
            if len(queens) == n:
                board = [(['.']*n) for _ in range(n)]
                for row in range(n):
                    for col in range(n):
                        if (row, col) in queens:
                            board[row][col] = 'Q'
                        else:
                            board[row][col] = '.'
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
                    queens.add((row, col))

                    # runs dfs
                    dfs(queens)

                    # reset values
                    queens.remove((row, col))
        
        dfs(set())

        return res