class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                edges.append((distance, i, j))

        edges.sort()
        minimum_cost = 0
        parent = list(range(n))
        edge_count = 0

        for distance, u, v in edges:
            if find(parent, u) != find(parent, v):
                union(parent, u, v)
                minimum_cost += distance
                edge_count += 1
                if edge_count == n - 1:
                    break

        return minimum_cost

def main():
    s = Solution()
    # Example usage:
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(s.minCostConnectPoints(points1))  # Output: 20

    points2 = [[3, 12], [-2, 5], [-4, 1]]
    print(s.minCostConnectPoints(points2))  # Output: 18
