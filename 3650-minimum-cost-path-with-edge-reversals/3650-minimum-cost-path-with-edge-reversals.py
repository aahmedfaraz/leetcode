import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        # Build adjacency list: original edges + reverse edges with 2*w cost
        for u, v, w in edges:
            adj[u].append((v, w))       # original
            adj[v].append((u, 2*w))     # reversed

        # Dijkstra's shortest path
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, w in adj[u]:
                nxt = cost + w
                if nxt < dist[v]:
                    dist[v] = nxt
                    heapq.heappush(pq, (nxt, v))

        return dist[n-1] if dist[n-1] < INF else -1
