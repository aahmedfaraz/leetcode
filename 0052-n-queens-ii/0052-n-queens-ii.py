class Solution:
    def totalNQueens(self, n: int) -> int:
        total = 0

        def dfs(queens):
            nonlocal total
            # If all queens are filled
            if len(queens) == n:
                total += 1
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
        return total