from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int: 
        # we need minimum cost to convert each letter from "source" to "target"
        # means we need shortest path from each letter to all other letters
        # like,
        # a -> b, c, d, ..., z
        # b -> a, c, d, ..., z
        # c -> a, b, d, ..., z
        # .
        # .
        # z -> a, b, c, ..., y

        # sounds like floyd warshal algorithm

        # initialize 2d array to store shortest path from each letter to 26 letters
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]

        # distance from a letter to itself is 0
        for i in range(26):
            dist[i][i] = 0

        # enter distance of direct connected nodes
        for i in range(len(original)):
            from_letter = ord(original[i]) - ord('a')
            to_letter = ord(changed[i]) - ord('a')
            dist[from_letter][to_letter] = min(dist[from_letter][to_letter], cost[i])

        # floyd warshall algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # calculate final cost
        res = 0
        for i in range(len(source)):
            from_letter = ord(source[i]) - ord('a')
            to_letter = ord(target[i]) - ord('a')
            if dist[from_letter][to_letter] == INF:
                return -1 # impossible transformation
            res += dist[from_letter][to_letter]

        return res

# Time complexity
# Floyd Warshall = O(26³) = O(1) constant
# Building graph = O(len(original))
# Final traversal = O(len(source))
# Total = O(len(source) + len(original))

# Space complexity
# Distance matrix = 26 × 26
# = O(1) constant space