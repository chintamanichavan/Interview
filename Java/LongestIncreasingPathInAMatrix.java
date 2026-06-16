public class LongestIncreasingPathInAMatrix {
    private int m, n;
    private int[][] grid;
    private int[][] memo;
    private static final int[][] DIRS = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

    public int longestIncreasingPath(int[][] matrix) {
        m = matrix.length;
        n = matrix[0].length;
        grid = matrix;
        memo = new int[m][n];
        int ans = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                ans = Math.max(ans, dfs(r, c));
        return ans;
    }

    private int dfs(int r, int c) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        for (int[] d : DIRS) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c]) {
                best = Math.max(best, 1 + dfs(nr, nc));
            }
        }
        return memo[r][c] = best;
    }

    public static void main(String[] args) {
        LongestIncreasingPathInAMatrix s = new LongestIncreasingPathInAMatrix();
        System.out.println(s.longestIncreasingPath(new int[][] { {9, 9, 4}, {6, 6, 8}, {2, 1, 1} }));  // 4
        System.out.println(s.longestIncreasingPath(new int[][] { {3, 4, 5}, {3, 2, 6}, {2, 2, 1} }));  // 4
        System.out.println(s.longestIncreasingPath(new int[][] { {1} }));                              // 1
    }
}
