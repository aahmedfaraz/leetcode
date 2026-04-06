class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))

        x = y = 0
        dx, dy = 0, 1  # north
        max_dist = 0

        for com in commands:
            if com == -2:  # left
                dx, dy = -dy, dx
            elif com == -1:  # right
                dx, dy = dy, -dx
            else:
                for _ in range(com):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles_set:
                        break
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist
