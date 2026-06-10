import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class FindKPairsWithSmallestSums {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums1.length == 0 || nums2.length == 0) return res;
        // min-heap of {sum, i, j}
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < nums1.length && i < k; i++) {
            heap.add(new int[] { nums1[i] + nums2[0], i, 0 });
        }
        while (!heap.isEmpty() && res.size() < k) {
            int[] cur = heap.poll();
            int i = cur[1], j = cur[2];
            res.add(List.of(nums1[i], nums2[j]));
            if (j + 1 < nums2.length) {
                heap.add(new int[] { nums1[i] + nums2[j + 1], i, j + 1 });
            }
        }
        return res;
    }

    public static void main(String[] args) {
        FindKPairsWithSmallestSums s = new FindKPairsWithSmallestSums();
        System.out.println(s.kSmallestPairs(new int[] { 1, 7, 11 }, new int[] { 2, 4, 6 }, 3)); // [[1, 2], [1, 4], [1, 6]]
        System.out.println(s.kSmallestPairs(new int[] { 1, 1, 2 }, new int[] { 1, 2, 3 }, 2));  // [[1, 1], [1, 1]]
        System.out.println(s.kSmallestPairs(new int[] { 1, 2 }, new int[] { 3 }, 3));           // [[1, 3], [2, 3]]
    }
}
