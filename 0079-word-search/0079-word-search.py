class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def check(row, col, chari, covered):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if chari < 0 or chari >= len(word):
                return False
            if (row, col) in covered:
                return False
            if board[row][col] == word[chari]:
                if chari == len(word) - 1:
                    return True
                else:
                    covered.add((row, col))
                    found = (
                        check(row+1, col, chari + 1, covered) or 
                        check(row-1, col, chari + 1, covered) or
                        check(row, col+1, chari + 1, covered) or
                        check(row, col-1, chari + 1, covered)
                    )
                    covered.remove((row, col))
                    return found
            else:
                return False

        for row in range(rows):
            for col in range(cols):
                if check(row, col, 0, set()):
                    return True
        
        return False