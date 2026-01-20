# Leetcode Problem 733: Flood Fill
# Link: https://leetcode.com/problems/flood-fill/description/

# Using DFS Approach

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image
        
        def dfs(r: int, c: int):
            # Boundary check
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return

            # Stop if color is not original
            if image[r][c] != originalColor:
                return

            # Change Color
            image[r][c] = newColor

            # Visit neighbors
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right
        
        dfs(sr, sc)
        return image

        # Time complexity: O(r x c) = O(n)
        # Space complexity: O(r x c) = O(n) -> Recursion



        