from collections import defaultdict
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Tree rooted at 1. DFS while propagating probability = 1 / (# unvisited neighbors at each step).
        # Reaching target at time s: if s == t, return prob; if s < t and target is a leaf (no
        # unvisited children), frog stays put forever, also return prob; otherwise frog must move on.
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * (n + 1)
        visited[1] = True

        def dfs(node: int, time: int, prob: float) -> float:
            children = [v for v in adj[node] if not visited[v]]
            if node == target:
                return prob if time == t or not children else 0.0
            if time == t or not children:
                return 0.0
            for c in children:
                visited[c] = True
                res = dfs(c, time + 1, prob / len(children))
                if res > 0:
                    return res
            return 0.0

        return dfs(1, 0, 1.0)


if __name__ == '__main__':
    s = Solution()
    edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    print(s.frogPosition(7, edges, 2, 4))  # 0.16666...
    print(s.frogPosition(7, edges, 1, 7))  # 0.33333...
    print(s.frogPosition(7, edges, 20, 6)) # 0.16666... (frog reaches 6 at t=2, stays)
    print(s.frogPosition(1, [], 1, 1))      # 1.0 (single vertex; frog never moves)
