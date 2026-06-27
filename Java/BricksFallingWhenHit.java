public class BricksFallingWhenHit {
    private int[] parent, sz;

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) {
            parent[ra] = rb;
            sz[rb] += sz[ra];
        }
    }

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int m = grid.length, n = grid[0].length;
        int top = m * n;
        parent = new int[m * n + 1];
        sz = new int[m * n + 1];
        for (int i = 0; i <= m * n; i++) {
            parent[i] = i;
            sz[i] = 1;
        }

        int[][] g = new int[m][n];
        for (int i = 0; i < m; i++) g[i] = grid[i].clone();
        for (int[] h : hits) g[h[0]][h[1]] = 0;

        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if (g[r][c] == 1) {
                    if (r == 0) union(r * n + c, top);
                    if (r > 0 && g[r - 1][c] == 1) union(r * n + c, (r - 1) * n + c);
                    if (c > 0 && g[r][c - 1] == 1) union(r * n + c, r * n + c - 1);
                }

        int[][] dirs = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
        int[] res = new int[hits.length];
        for (int i = hits.length - 1; i >= 0; i--) {
            int r = hits[i][0], c = hits[i][1];
            if (grid[r][c] == 0) continue;
            int before = sz[find(top)];
            g[r][c] = 1;
            if (r == 0) union(r * n + c, top);
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && g[nr][nc] == 1)
                    union(r * n + c, nr * n + nc);
            }
            int after = sz[find(top)];
            res[i] = Math.max(0, after - before - 1);
        }
        return res;
    }

    public static void main(String[] args) {
        BricksFallingWhenHit s = new BricksFallingWhenHit();
        System.out.println(java.util.Arrays.toString(
                s.hitBricks(new int[][] { {1, 0, 0, 0}, {1, 1, 1, 0} }, new int[][] { {1, 0} })));  // [2]
        System.out.println(java.util.Arrays.toString(
                s.hitBricks(new int[][] { {1, 0, 0, 0}, {1, 1, 0, 0} }, new int[][] { {1, 1}, {1, 0} })));  // [0, 0]
        System.out.println(java.util.Arrays.toString(
                s.hitBricks(new int[][] { {1, 1, 1}, {0, 1, 0}, {0, 0, 0} },
                        new int[][] { {0, 2}, {2, 0}, {0, 1}, {1, 2} })));  // [0, 0, 1, 0]
    }
}
