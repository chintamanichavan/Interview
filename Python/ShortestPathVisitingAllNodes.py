class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        
        # Initialize the dp array
        dp = [[float('inf')] * (1 << n) for _ in range(n)]
        
        # Initialize the starting node's distance
        for i in range(n):
            dp[i][1 << i] = 0
        
        # Iterate through all possible combinations of visited nodes
        for mask in range(1 << n):
            for u in range(n):
                if mask & (1 << u):
                    for v in graph[u]:
                        dp[u][mask] = min(dp[u][mask], dp[v][mask ^ (1 << u)] + 1)
        
        # Find the minimum distance to visit all nodes starting and ending at node 0
        min_distance = min(dp[i][(1 << n) - 1] for i in range(n))
        
        return min_distance

# Example usage:
graph1 = [[1, 2, 3], [0], [0], [0]]
print(shortestPathLength(graph1))  # Output: 4

graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
print(shortestPathLength(graph2))  # Output: 4
