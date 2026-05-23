import java.util.Arrays;

public class DungeonGame {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length, n = dungeon[0].length;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n - 1] = 1;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int need = Math.min(dp[j], dp[j + 1]) - dungeon[i][j];
                dp[j] = Math.max(need, 1);
            }
        }
        return dp[0];
    }

    public static void main(String[] args) {
        DungeonGame s = new DungeonGame();
        System.out.println(s.calculateMinimumHP(new int[][] { {-2, -3, 3}, {-5, -10, 1}, {10, 30, -5} })); // 7
        System.out.println(s.calculateMinimumHP(new int[][] { {0} }));   // 1
        System.out.println(s.calculateMinimumHP(new int[][] { {100} })); // 1
        System.out.println(s.calculateMinimumHP(new int[][] { {-3} }));  // 4
    }
}
