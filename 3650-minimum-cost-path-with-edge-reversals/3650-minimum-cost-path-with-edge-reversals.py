import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Build graph: normal edge (u->v, w) and reversed edge (v->u, 2*w)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        
        # Dijkstra's algorithm
        pq = [(0, 0)]  # (cost, node)
        min_costs = {0: 0}
        
        while pq:
            cost, u = heapq.heappop(pq)
            
            if cost > min_costs.get(u, float('inf')):
                continue
            
            if u == n - 1:
                return cost
                
            for v, weight in graph[u]:
                new_cost = cost + weight
                if new_cost < min_costs.get(v, float('inf')):
                    min_costs[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        return -1
