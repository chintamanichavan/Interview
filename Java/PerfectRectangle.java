import java.util.HashSet;
import java.util.Set;

public class PerfectRectangle {
    public boolean isRectangleCover(int[][] rectangles) {
        long area = 0;
        int minx = Integer.MAX_VALUE, miny = Integer.MAX_VALUE;
        int maxx = Integer.MIN_VALUE, maxy = Integer.MIN_VALUE;
        Set<String> corners = new HashSet<>();

        for (int[] r : rectangles) {
            int x1 = r[0], y1 = r[1], x2 = r[2], y2 = r[3];
            area += (long) (x2 - x1) * (y2 - y1);
            minx = Math.min(minx, x1);
            miny = Math.min(miny, y1);
            maxx = Math.max(maxx, x2);
            maxy = Math.max(maxy, y2);
            for (String p : new String[] { key(x1, y1), key(x1, y2), key(x2, y1), key(x2, y2) }) {
                if (!corners.add(p)) corners.remove(p);
            }
        }

        Set<String> expected = new HashSet<>();
        expected.add(key(minx, miny));
        expected.add(key(minx, maxy));
        expected.add(key(maxx, miny));
        expected.add(key(maxx, maxy));
        if (!corners.equals(expected)) return false;
        return area == (long) (maxx - minx) * (maxy - miny);
    }

    private String key(int x, int y) {
        return x + "," + y;
    }

    public static void main(String[] args) {
        PerfectRectangle s = new PerfectRectangle();
        System.out.println(s.isRectangleCover(new int[][] { {1, 1, 3, 3}, {3, 1, 4, 2}, {3, 2, 4, 4}, {1, 3, 2, 4}, {2, 3, 3, 4} })); // true
        System.out.println(s.isRectangleCover(new int[][] { {1, 1, 2, 3}, {1, 3, 2, 4}, {3, 1, 4, 2}, {3, 2, 4, 4} })); // false
        System.out.println(s.isRectangleCover(new int[][] { {1, 1, 3, 3}, {3, 1, 4, 2}, {1, 3, 2, 4}, {2, 2, 4, 4} })); // false
        System.out.println(s.isRectangleCover(new int[][] { {0, 0, 1, 1} })); // true
    }
}
