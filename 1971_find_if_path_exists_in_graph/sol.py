from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = { i: [] for i in range(n) }

        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = set([source])

        # Breadth First Search
        while queue:
            vertex = queue.popleft()

            # Perform any operation with the vertex
            if vertex == destination:
                return True

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False

# Example usage:
Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for the graph representation and the visited set.

# OUTPUT:
# True
# False

