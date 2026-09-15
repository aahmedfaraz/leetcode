class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        wordset = set(words)
        maxdep = max(map(len, words))
        directions = [ # row, col
            (0, 1), # right
            (0, -1), # left
            (1, 0), # down
            (-1, 0), # up
        ]
        strings = set()
        visited = set()
        curr = []

        def dfs(row, col):
            if len(strings) == len(words):
                return

            if row >= rows or col >= cols or row < 0 or col < 0:
                return

            curr.append(board[row][col])
            w = "".join(curr)

            if w in wordset:
                strings.add(w)

            if len(curr) < maxdep:
                visited.add((row, col))
                for dr, dc in directions:
                    newrow = row + dr
                    newcol = col + dc
                    if newrow >= rows or newcol >= cols or newrow < 0 or newcol < 0:
                        continue
                    if (newrow, newcol) in visited:
                        continue
                    dfs(newrow, newcol)

                visited.remove((row, col))
            curr.pop()
        
        for r in range(rows):
            for c in range(cols):
                if len(strings) != len(words):
                    dfs(r, c)

        return list(strings)