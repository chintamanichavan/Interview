import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class JumpGameIII {
    public boolean canReach(int[] arr, int start) {
        int n = arr.length;
        boolean[] seen = new boolean[n];
        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        seen[start] = true;
        while (!queue.isEmpty()) {
            int i = queue.poll();
            if (arr[i] == 0) return true;
            for (int j : new int[] { i + arr[i], i - arr[i] }) {
                if (j >= 0 && j < n && !seen[j]) {
                    seen[j] = true;
                    queue.add(j);
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        JumpGameIII s = new JumpGameIII();
        System.out.println(s.canReach(new int[] { 4, 2, 3, 0, 3, 1, 2 }, 5)); // true
        System.out.println(s.canReach(new int[] { 4, 2, 3, 0, 3, 1, 2 }, 0)); // true
        System.out.println(s.canReach(new int[] { 3, 0, 2, 1, 2 }, 2));       // false
    }
}
