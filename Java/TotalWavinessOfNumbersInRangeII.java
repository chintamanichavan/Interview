public class TotalWavinessOfNumbersInRangeII {
    private String s;
    private int L;
    // memo[pos][started][prev2+1][prev1+1]
    private boolean[][][][] visited;
    private long[][][][] cnt;
    private long[][][][] tot;

    public long totalWaviness(long num1, long num2) {
        return wavinessUpTo(num2) - wavinessUpTo(num1 - 1);
    }

    private long wavinessUpTo(long n) {
        if (n < 0) return 0;
        s = Long.toString(n);
        L = s.length();
        visited = new boolean[L][2][11][11];
        cnt = new long[L][2][11][11];
        tot = new long[L][2][11][11];
        long[] r = dp(0, false, -1, -1, true);
        return r[1];
    }

    private long[] dp(int pos, boolean started, int prev2, int prev1, boolean tight) {
        if (pos == L) return new long[] { 1, 0 };
        int si = started ? 1 : 0;
        if (!tight && visited[pos][si][prev2 + 1][prev1 + 1]) {
            return new long[] { cnt[pos][si][prev2 + 1][prev1 + 1], tot[pos][si][prev2 + 1][prev1 + 1] };
        }
        int limit = tight ? (s.charAt(pos) - '0') : 9;
        long c = 0, t = 0;
        for (int d = 0; d <= limit; d++) {
            boolean ntight = tight && d == limit;
            boolean nstarted;
            int np2, np1, event = 0;
            if (!started && d == 0) {
                nstarted = false; np2 = -1; np1 = -1;
            } else {
                nstarted = true;
                if (prev1 != -1 && prev2 != -1
                        && ((prev1 > prev2 && prev1 > d) || (prev1 < prev2 && prev1 < d))) {
                    event = 1;
                }
                np2 = prev1; np1 = d;
            }
            long[] sub = dp(pos + 1, nstarted, np2, np1, ntight);
            c += sub[0];
            t += sub[1] + (long) event * sub[0];
        }
        if (!tight) {
            visited[pos][si][prev2 + 1][prev1 + 1] = true;
            cnt[pos][si][prev2 + 1][prev1 + 1] = c;
            tot[pos][si][prev2 + 1][prev1 + 1] = t;
        }
        return new long[] { c, t };
    }

    public static void main(String[] args) {
        TotalWavinessOfNumbersInRangeII s = new TotalWavinessOfNumbersInRangeII();
        System.out.println(s.totalWaviness(120, 130));               // 3
        System.out.println(s.totalWaviness(198, 202));               // 3
        System.out.println(s.totalWaviness(4848, 4848));             // 2
        System.out.println(s.totalWaviness(1, 1000000L));            // 2230005
        System.out.println(s.totalWaviness(1, 1000000000000000L));   // 7360000000000005
    }
}
