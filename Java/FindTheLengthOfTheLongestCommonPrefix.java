import java.util.HashSet;
import java.util.Set;

public class FindTheLengthOfTheLongestCommonPrefix {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        Set<Integer> prefixes = new HashSet<>();
        for (int x : arr1) {
            while (x > 0) {
                prefixes.add(x);
                x /= 10;
            }
        }

        int best = 0;
        for (int y : arr2) {
            while (y > 0) {
                if (prefixes.contains(y)) {
                    best = Math.max(best, digits(y));
                    break;
                }
                y /= 10;
            }
        }
        return best;
    }

    private static int digits(int n) {
        int d = 0;
        while (n > 0) { d++; n /= 10; }
        return d;
    }

    public static void main(String[] args) {
        FindTheLengthOfTheLongestCommonPrefix s = new FindTheLengthOfTheLongestCommonPrefix();
        System.out.println(s.longestCommonPrefix(new int[] { 1, 10, 100 }, new int[] { 1000 })); // 3
        System.out.println(s.longestCommonPrefix(new int[] { 1, 2, 3 }, new int[] { 4, 4, 4 })); // 0
        System.out.println(s.longestCommonPrefix(new int[] { 1 }, new int[] { 1 }));             // 1
    }
}
