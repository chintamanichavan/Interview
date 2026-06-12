import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;

public class MaximumTotalSubarrayValueII {
    public long maxTotalValue(int[] nums, int k) {
        int n = nums.length;
        int[] logt = new int[n + 1];
        for (int i = 2; i <= n; i++) logt[i] = logt[i / 2] + 1;

        List<int[]> upMax = new ArrayList<>();
        List<int[]> upMin = new ArrayList<>();
        upMax.add(nums.clone());
        upMin.add(nums.clone());
        for (int j = 1; (1 << j) <= n; j++) {
            int half = 1 << (j - 1), length = 1 << j;
            int[] pmx = upMax.get(j - 1), pmn = upMin.get(j - 1);
            int[] cmx = new int[n - length + 1];
            int[] cmn = new int[n - length + 1];
            for (int i = 0; i + length <= n; i++) {
                cmx[i] = Math.max(pmx[i], pmx[i + half]);
                cmn[i] = Math.min(pmn[i], pmn[i + half]);
            }
            upMax.add(cmx);
            upMin.add(cmn);
        }

        // max-heap of {value, l, r}
        PriorityQueue<int[]> heap = new PriorityQueue<>((x, y) -> Integer.compare(y[0], x[0]));
        Set<Long> seen = new HashSet<>();
        heap.add(new int[] { value(upMax, upMin, logt, 0, n - 1), 0, n - 1 });
        seen.add((long) (n - 1));  // key = l*n + r, l=0
        long total = 0;
        for (int i = 0; i < k; i++) {
            int[] cur = heap.poll();
            int v = cur[0], l = cur[1], r = cur[2];
            total += v;
            if (l + 1 <= r && seen.add((long) (l + 1) * n + r)) {
                heap.add(new int[] { value(upMax, upMin, logt, l + 1, r), l + 1, r });
            }
            if (l <= r - 1 && seen.add((long) l * n + (r - 1))) {
                heap.add(new int[] { value(upMax, upMin, logt, l, r - 1), l, r - 1 });
            }
        }
        return total;
    }

    private int value(List<int[]> upMax, List<int[]> upMin, int[] logt, int l, int r) {
        int j = logt[r - l + 1], shift = 1 << j;
        int mx = Math.max(upMax.get(j)[l], upMax.get(j)[r - shift + 1]);
        int mn = Math.min(upMin.get(j)[l], upMin.get(j)[r - shift + 1]);
        return mx - mn;
    }

    public static void main(String[] args) {
        MaximumTotalSubarrayValueII s = new MaximumTotalSubarrayValueII();
        System.out.println(s.maxTotalValue(new int[] { 1, 3, 2 }, 2));     // 4
        System.out.println(s.maxTotalValue(new int[] { 4, 2, 5, 1 }, 3));  // 12
        System.out.println(s.maxTotalValue(new int[] { 1 }, 1));           // 0
    }
}
