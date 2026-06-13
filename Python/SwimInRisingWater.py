import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # At time t you may stand on any cell with elevation <= t. The answer is the path from
        # (0,0) to (n-1,n-1) that minimizes the maximum cell elevation along it -> Dijkstra where
        # the "distance" of a path is its max elevation. O(n^2 log n).
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = [[False] * n for _ in range(n)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            if seen[r][c]:
                continue
            seen[r][c] = True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.swimInWater([[0, 2], [1, 3]]))  # 3
    print(
        s.swimInWater(
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
    )  # 16
    print(s.swimInWater([[0]]))  # 0
