import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public class RaceCar {
    public int racecar(int target) {
        int bound = 2 * target;
        Set<Long> seen = new HashSet<>();
        seen.add(key(0, 1));
        Queue<int[]> q = new ArrayDeque<>();  // {pos, speed, steps}
        q.add(new int[] { 0, 1, 0 });
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int pos = cur[0], speed = cur[1], steps = cur[2];
            if (pos == target) return steps;
            // 'A'
            int npos = pos + speed, nspeed = speed * 2;
            if (npos >= -bound && npos <= bound && seen.add(key(npos, nspeed))) {
                q.add(new int[] { npos, nspeed, steps + 1 });
            }
            // 'R'
            int rspeed = speed > 0 ? -1 : 1;
            if (seen.add(key(pos, rspeed))) {
                q.add(new int[] { pos, rspeed, steps + 1 });
            }
        }
        return -1;
    }

    private long key(int pos, int speed) {
        return ((long) pos << 32) ^ (speed & 0xffffffffL);
    }

    public static void main(String[] args) {
        RaceCar s = new RaceCar();
        System.out.println(s.racecar(3));  // 2
        System.out.println(s.racecar(6));  // 5
        System.out.println(s.racecar(1));  // 1
        System.out.println(s.racecar(4));  // 5
    }
}
