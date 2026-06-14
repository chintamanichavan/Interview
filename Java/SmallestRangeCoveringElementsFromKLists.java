import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class SmallestRangeCoveringElementsFromKLists {
    public int[] smallestRange(List<List<Integer>> nums) {
        // min-heap of {val, listIndex, idx}
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int curMax = Integer.MIN_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            int v = nums.get(i).get(0);
            heap.add(new int[] { v, i, 0 });
            curMax = Math.max(curMax, v);
        }
        int[] best = { heap.peek()[0], curMax };
        while (true) {
            int[] cur = heap.poll();
            int val = cur[0], i = cur[1], j = cur[2];
            if (curMax - val < best[1] - best[0]) best = new int[] { val, curMax };
            if (j + 1 == nums.get(i).size()) break;
            int nxt = nums.get(i).get(j + 1);
            curMax = Math.max(curMax, nxt);
            heap.add(new int[] { nxt, i, j + 1 });
        }
        return best;
    }

    public static void main(String[] args) {
        SmallestRangeCoveringElementsFromKLists s = new SmallestRangeCoveringElementsFromKLists();
        System.out.println(Arrays.toString(s.smallestRange(List.of(
                List.of(4, 10, 15, 24, 26), List.of(0, 9, 12, 20), List.of(5, 18, 22, 30)))));  // [20, 24]
        System.out.println(Arrays.toString(s.smallestRange(List.of(
                List.of(1, 2, 3), List.of(1, 2, 3), List.of(1, 2, 3)))));                        // [1, 1]
        System.out.println(Arrays.toString(s.smallestRange(List.of(
                List.of(1), List.of(2), List.of(3)))));                                          // [1, 3]
    }
}
