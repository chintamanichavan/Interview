import java.util.ArrayList;
import java.util.List;

public class TwentyFourGame {
    private static final double EPS = 1e-6;

    public boolean judgePoint24(int[] cards) {
        List<Double> nums = new ArrayList<>();
        for (int c : cards) nums.add((double) c);
        return solve(nums);
    }

    private boolean solve(List<Double> nums) {
        int n = nums.size();
        if (n == 1) return Math.abs(nums.get(0) - 24.0) < EPS;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                List<Double> rest = new ArrayList<>();
                for (int x = 0; x < n; x++)
                    if (x != i && x != j) rest.add(nums.get(x));
                double a = nums.get(i), b = nums.get(j);
                List<Double> cands = new ArrayList<>(List.of(a + b, a - b, a * b));
                if (Math.abs(b) > EPS) cands.add(a / b);
                for (double val : cands) {
                    rest.add(val);
                    if (solve(rest)) return true;
                    rest.remove(rest.size() - 1);
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        TwentyFourGame s = new TwentyFourGame();
        System.out.println(s.judgePoint24(new int[] { 4, 1, 8, 7 }));  // true
        System.out.println(s.judgePoint24(new int[] { 1, 2, 1, 2 }));  // false
        System.out.println(s.judgePoint24(new int[] { 3, 3, 8, 8 }));  // true
        System.out.println(s.judgePoint24(new int[] { 1, 1, 1, 1 }));  // false
    }
}
