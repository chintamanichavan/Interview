from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Exhaustive backtracking. maxTime <= 100 and every edge costs >= 10, so a path has
        # at most 10 edges; with degree <= 4 the search tree is <= 4^10, pruned by remaining
        # time. visited[v] counts active visits so each node's value is added exactly once.
        n = len(values)
        adj: List[List[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        visited = [0] * n
        best = 0

        def dfs(node: int, time_left: int, quality: int) -> None:
            nonlocal best
            if node == 0:
                best = max(best, quality)
            for v, t in adj[node]:
                if t <= time_left:
                    gain = values[v] if visited[v] == 0 else 0
                    visited[v] += 1
                    dfs(v, time_left - t, quality + gain)
                    visited[v] -= 1

        visited[0] = 1
        dfs(0, maxTime, values[0])
        return best


if __name__ == '__main__':
    s = Solution()
    print(s.maximalPathQuality([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49))  # 75
    print(s.maximalPathQuality([5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30))  # 25
    print(s.maximalPathQuality([1, 2, 3, 4],
                               [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50))        # 7
    print(s.maximalPathQuality([5], [], 100))                                                # 5
