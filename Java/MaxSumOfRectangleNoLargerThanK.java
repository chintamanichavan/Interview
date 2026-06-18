import java.util.TreeSet;

public class MaxSumOfRectangleNoLargerThanK {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        long best = Long.MIN_VALUE;
        for (int left = 0; left < n; left++) {
            long[] rowsum = new long[m];
            for (int right = left; right < n; right++) {
                for (int i = 0; i < m; i++) rowsum[i] += matrix[i][right];
                TreeSet<Long> prefixes = new TreeSet<>();
                prefixes.add(0L);
                long cur = 0;
                for (long v : rowsum) {
                    cur += v;
                    Long p = prefixes.ceiling(cur - k);  // smallest prefix >= cur - k
                    if (p != null) best = Math.max(best, cur - p);
                    prefixes.add(cur);
                }
            }
        }
        return (int) best;
    }

    public static void main(String[] args) {
        MaxSumOfRectangleNoLargerThanK s = new MaxSumOfRectangleNoLargerThanK();
        System.out.println(s.maxSumSubmatrix(new int[][] { {1, 0, 1}, {0, -2, 3} }, 2));  // 2
        System.out.println(s.maxSumSubmatrix(new int[][] { {2, 2, -1} }, 3));             // 3
        System.out.println(s.maxSumSubmatrix(new int[][] { {2, 2, -1} }, 0));             // -1
    }
}
