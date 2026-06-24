import java.util.HashSet;
import java.util.Set;

public class CrackingTheSafe {
    private int k;
    private StringBuilder path;
    private Set<String> seen;

    public String crackSafe(int n, int k) {
        if (n == 1) {
            StringBuilder s = new StringBuilder();
            for (int d = 0; d < k; d++) s.append(d);
            return s.toString();
        }
        this.k = k;
        path = new StringBuilder();
        seen = new HashSet<>();
        String start = "0".repeat(n - 1);
        dfs(start);
        return path.append(start).toString();
    }

    private void dfs(String node) {
        for (int d = 0; d < k; d++) {
            String edge = node + d;
            if (!seen.contains(edge)) {
                seen.add(edge);
                dfs(edge.substring(1));
                path.append(d);
            }
        }
    }

    public static void main(String[] args) {
        CrackingTheSafe s = new CrackingTheSafe();
        System.out.println(s.crackSafe(1, 2));  // 01
        System.out.println(s.crackSafe(2, 2));  // 01100
        System.out.println(s.crackSafe(3, 2));  // 0011101000
        System.out.println(s.crackSafe(2, 3));  // 0221120100
    }
}
