public class StoneGameVIII {
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        long[] prefix = new long[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += stones[i];
            prefix[i] = sum;
        }
        long dp = prefix[n - 1];
        for (int i = n - 2; i >= 1; i--) {
            dp = Math.max(dp, prefix[i] - dp);
        }
        return (int) dp;
    }

    public static void main(String[] args) {
        StoneGameVIII s = new StoneGameVIII();
        System.out.println(s.stoneGameVIII(new int[] { -1, 2, -3, 4, -5 }));        // 5
        System.out.println(s.stoneGameVIII(new int[] { 7, -6, 5, 10, 5, -2, -6 })); // 13
        System.out.println(s.stoneGameVIII(new int[] { -10, -12 }));                // -22
    }
}
