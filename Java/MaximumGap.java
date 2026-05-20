public class MaximumGap {
    public int maximumGap(int[] nums) {
        int n = nums.length;
        if (n < 2) return 0;
        int mn = nums[0], mx = nums[0];
        for (int x : nums) {
            if (x < mn) mn = x;
            if (x > mx) mx = x;
        }
        if (mn == mx) return 0;

        // Pigeonhole: max gap >= ceil((mx-mn)/(n-1)), so it lies between buckets of that size.
        int bucketSize = Math.max(1, (mx - mn) / (n - 1));
        int numBuckets = (mx - mn) / bucketSize + 1;
        int[] bMin = new int[numBuckets];
        int[] bMax = new int[numBuckets];
        boolean[] seen = new boolean[numBuckets];

        for (int x : nums) {
            int i = (x - mn) / bucketSize;
            if (!seen[i]) {
                bMin[i] = x;
                bMax[i] = x;
                seen[i] = true;
            } else {
                bMin[i] = Math.min(bMin[i], x);
                bMax[i] = Math.max(bMax[i], x);
            }
        }

        int best = 0, prevMax = mn;
        for (int i = 0; i < numBuckets; i++) {
            if (!seen[i]) continue;
            best = Math.max(best, bMin[i] - prevMax);
            prevMax = bMax[i];
        }
        return best;
    }

    public static void main(String[] args) {
        MaximumGap s = new MaximumGap();
        System.out.println(s.maximumGap(new int[] { 3, 6, 9, 1 }));  // 3
        System.out.println(s.maximumGap(new int[] { 10 }));          // 0
        System.out.println(s.maximumGap(new int[] { 1, 1, 1, 1 }));  // 0
        System.out.println(s.maximumGap(new int[] { 1, 10000000 })); // 9999999
    }
}
