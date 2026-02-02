import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Build graph: normal edge (u->v, w) and reversed edge (v->u, 2*w)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        
        # Dijkstra algorithm
        pq = [(0, 0)]  # (cost, node)
        min_costs = {
            0: 0
        }
        
        while pq:
            cost, u = heapq.heappop(pq)
            
            # if we are already have min cost of this node
            if cost > min_costs.get(u, float('inf')):
                continue
            
            # Base case - found target node
            if u == n - 1:
                return cost
            
            # check cost with all neighbours
            for v, weight in graph[u]:
                new_cost = cost + weight
                # found less cost with a neighbour
                if new_cost < min_costs.get(v, float('inf')):
                    min_costs[v] = new_cost # update min cost
                    heapq.heappush(pq, (new_cost, v)) # push this node with updated cost in heap
                    
        return -1

# Time complexity = O(E log V) = O(n log n)
# Space complexity = O(V + E) = O(n)
