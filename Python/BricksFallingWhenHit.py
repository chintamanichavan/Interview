from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # Bricks survive iff connected to the top row. Erasing forward is hard (cascading falls),
        # so process in reverse: remove all hit bricks, union the rest, then re-add hits one by one.
        # Each re-add that newly connects to the top "saves" bricks = (top-size growth) - 1.
        m, n = len(grid), len(grid[0])
        TOP = m * n  # virtual node for the top

        parent = list(range(m * n + 1))
        size = [1] * (m * n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                size[rb] += size[ra]

        def idx(r, c):
            return r * n + c

        # Copy grid and remove hit bricks (only where a brick actually exists).
        g = [row[:] for row in grid]
        for r, c in hits:
            g[r][c] = 0

        # Union the surviving bricks; top-row bricks attach to TOP.
        for r in range(m):
            for c in range(n):
                if g[r][c] == 1:
                    if r == 0:
                        union(idx(r, c), TOP)
                    if r > 0 and g[r - 1][c] == 1:
                        union(idx(r, c), idx(r - 1, c))
                    if c > 0 and g[r][c - 1] == 1:
                        union(idx(r, c), idx(r, c - 1))

        res = [0] * len(hits)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 0:
                continue  # no brick was actually here; this hit does nothing
            before = size[find(TOP)]
            g[r][c] = 1
            if r == 0:
                union(idx(r, c), TOP)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and g[nr][nc] == 1:
                    union(idx(r, c), idx(nr, nc))
            after = size[find(TOP)]
            res[i] = max(0, after - before - 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]))  # [2]
    print(s.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]))  # [0, 0]
    print(
        s.hitBricks([[1, 1, 1], [0, 1, 0], [0, 0, 0]], [[0, 2], [2, 0], [0, 1], [1, 2]])
    )  # [0, 0, 1, 0]
