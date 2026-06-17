public class SplitArrayLargestSum {
    public int splitArray(int[] nums, int k) {
        long lo = 0, hi = 0;
        for (int x : nums) {
            lo = Math.max(lo, x);
            hi += x;
        }
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (needed(nums, mid) <= k) hi = mid;
            else lo = mid + 1;
        }
        return (int) lo;
    }

    private int needed(int[] nums, long cap) {
        int count = 1;
        long cur = 0;
        for (int x : nums) {
            if (cur + x > cap) {
                count++;
                cur = x;
            } else {
                cur += x;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        SplitArrayLargestSum s = new SplitArrayLargestSum();
        System.out.println(s.splitArray(new int[] { 7, 2, 5, 10, 8 }, 2));  // 18
        System.out.println(s.splitArray(new int[] { 1, 2, 3, 4, 5 }, 2));   // 9
        System.out.println(s.splitArray(new int[] { 1, 4, 4 }, 3));         // 4
    }
}
