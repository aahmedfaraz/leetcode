class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def transform(value):
            if value == 1 or value == 0: return value
            if value == 2:
                return 1
            else:
                return 0

        def transformAns(value):
            if value == 1 or value == 0: return value
            if value == 2:
                return 0
            else:
                return 1

        for row in range(rows):
            for col in range(cols):
                up, down, left, right, tleft, tright, bleft, bright = 0, 0, 0, 0, 0, 0, 0, 0
                if row > 0:
                    up = transform(board[row-1][col])
                    if col > 0:
                        tleft = transform(board[row-1][col-1])
                    if col < cols-1:
                        tright = transform(board[row-1][col+1])
                if row < rows-1:
                    down = transform(board[row+1][col])
                    if col > 0:
                        bleft = transform(board[row+1][col-1])
                    if col < cols-1:
                        bright = transform(board[row+1][col+1])
                if col > 0:
                    left = transform(board[row][col-1])
                if col < cols-1:
                    right = transform(board[row][col+1])
                
                allneighbours = up + down + left + right + tleft + tright + bleft + bright

                if (board[row][col] == 1 or board[row][col] == 2):
                    if allneighbours < 2 or allneighbours > 3:
                        board[row][col] = 2 # 2 => in reality is 1, but in ans its 0
                else:
                    if allneighbours == 3:
                        board[row][col] = 3 # 3 => in reality is 0, but in ans its 1
        
        for row in range(rows):
            for col in range(cols):
                board[row][col] = transformAns(board[row][col])

# Time = O(rows x cols)
# Space = O(1) auxiliary space