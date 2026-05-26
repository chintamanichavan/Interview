import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class TheSkylineProblem {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        // Events: {x, negH, r}. Negative h sorts starts before ends at the same x;
        // taller starts first.
        int[][] events = new int[buildings.length * 2][3];
        int k = 0;
        for (int[] b : buildings) {
            events[k++] = new int[] { b[0], -b[2], b[1] };
            events[k++] = new int[] { b[1], 0, 0 };
        }
        Arrays.sort(events, (a, c) -> {
            if (a[0] != c[0]) return Integer.compare(a[0], c[0]);
            return Integer.compare(a[1], c[1]);
        });

        // Max-heap on (height, end_x). Sentinel keeps it non-empty.
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, c) -> Integer.compare(c[0], a[0]));
        heap.offer(new int[] { 0, Integer.MAX_VALUE });

        List<List<Integer>> result = new ArrayList<>();
        for (int[] e : events) {
            int x = e[0], negH = e[1], r = e[2];
            if (negH != 0) heap.offer(new int[] { -negH, r });
            while (heap.peek()[1] <= x) heap.poll();
            int curMax = heap.peek()[0];
            if (result.isEmpty() || result.get(result.size() - 1).get(1) != curMax) {
                result.add(Arrays.asList(x, curMax));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        TheSkylineProblem s = new TheSkylineProblem();
        System.out.println(s.getSkyline(new int[][] { {2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8} }));
        System.out.println(s.getSkyline(new int[][] { {0, 2, 3}, {2, 5, 3} }));
        System.out.println(s.getSkyline(new int[][] { {1, 2, 1}, {1, 2, 2}, {1, 2, 3} }));
        System.out.println(s.getSkyline(new int[][] { {0, 3, 3}, {1, 5, 3}, {2, 4, 3}, {3, 7, 3} }));
    }
}
