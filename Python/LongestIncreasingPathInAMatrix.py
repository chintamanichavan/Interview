from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # memo[r][c] = longest strictly-increasing path starting at (r,c). The "increasing"
        # constraint makes the graph a DAG, so memoized DFS has no cycles. O(m*n).
        m, n = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)
        def dfs(r: int, c: int) -> int:
            best = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        return max(dfs(r, c) for r in range(m) for c in range(n))


if __name__ == "__main__":
    s = Solution()
    print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))  # 4
    print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))  # 4
    print(s.longestIncreasingPath([[1]]))  # 1
