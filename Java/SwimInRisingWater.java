import java.util.PriorityQueue;

public class SwimInRisingWater {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        // min-heap of {time, r, c}
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        boolean[][] seen = new boolean[n][n];
        heap.add(new int[] { grid[0][0], 0, 0 });
        int[][] dirs = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int t = cur[0], r = cur[1], c = cur[2];
            if (r == n - 1 && c == n - 1) return t;
            if (seen[r][c]) continue;
            seen[r][c] = true;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc]) {
                    heap.add(new int[] { Math.max(t, grid[nr][nc]), nr, nc });
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        SwimInRisingWater s = new SwimInRisingWater();
        System.out.println(s.swimInWater(new int[][] { {0, 2}, {1, 3} }));  // 3
        System.out.println(s.swimInWater(new int[][] { {0, 1, 2, 3, 4}, {24, 23, 22, 21, 5},
                {12, 13, 14, 15, 16}, {11, 17, 18, 19, 20}, {10, 9, 8, 7, 6} }));  // 16
        System.out.println(s.swimInWater(new int[][] { {0} }));  // 0
    }
}
