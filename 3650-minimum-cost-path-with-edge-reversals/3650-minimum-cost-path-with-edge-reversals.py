import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list with forward and reverse edges
        graph = defaultdict(list)
        for u, v, w in edges:
            # forward edge with cost w
            graph[u].append((v, w))
            # reversed edge with cost 2*w
            graph[v].append((u, 2 * w))

        # distances array
        dist = [float('inf')] * n
        dist[0] = 0

        # priority queue (cost, node)
        pq = [(0, 0)]

        while pq:
            cost, node = heapq.heappop(pq)
            if cost > dist[node]:
                continue
            if node == n - 1:
                return cost  # reached destination

            # relax neighbors
            for nxt, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))

        return -1 if dist[n - 1] == float('inf') else dist[n - 1]
