import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

public class SlidingPuzzle {
    private static final int[][] NEIGHBORS = {
            {1, 3}, {0, 2, 4}, {1, 5},
            {0, 4}, {1, 3, 5}, {2, 4}
    };

    public int slidingPuzzle(int[][] board) {
        char[] start = new char[6];
        int zero = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                int idx = i * 3 + j;
                start[idx] = (char) ('0' + board[i][j]);
                if (board[i][j] == 0) zero = idx;
            }
        }
        String startStr = new String(start);
        String target = "123450";
        if (startStr.equals(target)) return 0;

        Deque<int[]> queue = new ArrayDeque<>();
        Deque<String> states = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        states.add(startStr);
        queue.add(new int[] { zero, 0 });
        seen.add(startStr);
        while (!states.isEmpty()) {
            String state = states.poll();
            int[] meta = queue.poll();
            int z = meta[0], steps = meta[1];
            for (int nb : NEIGHBORS[z]) {
                char[] arr = state.toCharArray();
                char tmp = arr[z]; arr[z] = arr[nb]; arr[nb] = tmp;
                String nxt = new String(arr);
                if (nxt.equals(target)) return steps + 1;
                if (seen.add(nxt)) {
                    states.add(nxt);
                    queue.add(new int[] { nb, steps + 1 });
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        SlidingPuzzle s = new SlidingPuzzle();
        System.out.println(s.slidingPuzzle(new int[][] { {1, 2, 3}, {4, 0, 5} })); // 1
        System.out.println(s.slidingPuzzle(new int[][] { {1, 2, 3}, {5, 4, 0} })); // -1
        System.out.println(s.slidingPuzzle(new int[][] { {4, 1, 2}, {5, 0, 3} })); // 5
        System.out.println(s.slidingPuzzle(new int[][] { {1, 2, 3}, {4, 5, 0} })); // 0
    }
}
