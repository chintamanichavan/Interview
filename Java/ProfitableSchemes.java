public class ProfitableSchemes {
    private static final int MOD = 1_000_000_007;

    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int[][] dp = new int[n + 1][minProfit + 1];
        dp[0][0] = 1;
        for (int i = 0; i < group.length; i++) {
            int g = group[i], p = profit[i];
            for (int j = n; j >= g; j--) {
                for (int k = minProfit; k >= 0; k--) {
                    if (dp[j - g][k] == 0) continue;
                    int nk = Math.min(k + p, minProfit);
                    dp[j][nk] = (dp[j][nk] + dp[j - g][k]) % MOD;
                }
            }
        }
        long total = 0;
        for (int j = 0; j <= n; j++) total = (total + dp[j][minProfit]) % MOD;
        return (int) total;
    }

    public static void main(String[] args) {
        ProfitableSchemes s = new ProfitableSchemes();
        System.out.println(s.profitableSchemes(5, 3, new int[] { 2, 2 }, new int[] { 2, 3 }));        // 2
        System.out.println(s.profitableSchemes(10, 5, new int[] { 2, 3, 5 }, new int[] { 6, 7, 8 })); // 7
        System.out.println(s.profitableSchemes(1, 1, new int[] { 1, 1 }, new int[] { 1, 1 }));        // 2
    }
}
