# Leetcode Problem 733: Flood Fill
# Link: https://leetcode.com/problems/flood-fill/description/

# Using BFS Approach - Much safer than DFS for large inputs - avoids stack overflow

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = newColor

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == originalColor:
                        image[nr][nc] = newColor
                        queue.append((nr, nc))

        return image

        # Time complexity: O(r x c) = O(n)
        # Space complexity: O(r x c) = O(n) -> Queue