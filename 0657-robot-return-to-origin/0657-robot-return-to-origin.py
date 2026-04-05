class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]
        end = [0, 0]
        for move in moves:
            if move == 'U':
                start[1] += 1
            elif move == 'D':
                start[1] -= 1
            elif move == 'L':
                start[0] -= 1
            else:
                start[0] += 1
        return start == end