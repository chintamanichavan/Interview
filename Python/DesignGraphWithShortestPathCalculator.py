import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = {i: [] for i in range(n)}
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # Dijkstra's algorithm
        visited = [False] * self.n
        distances = [float('inf')] * self.n
        distances[node1] = 0
        min_heap = [(0, node1)]

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if visited[node]:
                continue

            visited[node] = True
            if node == node2:
                return dist

            for neighbor, edge_cost in self.graph[node]:
                if not visited[neighbor] and dist + edge_cost < distances[neighbor]:
                    distances[neighbor] = dist + edge_cost
                    heapq.heappush(min_heap, (distances[neighbor], neighbor))

        return -1 if distances[node2] == float('inf') else distances[node2]



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
