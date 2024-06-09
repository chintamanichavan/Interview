from typing import List
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))

        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))

def main():
    s = Solution()
    # Example usage:
    graph1 = [[1, 2, 3], [0], [0], [0]]
    print(s.shortestPathLength(graph1))  # Output: 4

    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(s.shortestPathLength(graph2))  # Output: 4

if __name__ == '__main__':
    main()
