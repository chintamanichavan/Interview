import java.util.HashSet;
import java.util.Set;

public class FindTheClosestPalindrome {
    public String nearestPalindromic(String n) {
        int length = n.length();
        long num = Long.parseLong(n);
        Set<Long> cands = new HashSet<>();
        cands.add(pow10(length - 1) - 1);
        cands.add(pow10(length) + 1);

        long prefix = Long.parseLong(n.substring(0, (length + 1) / 2));
        for (long p : new long[] { prefix - 1, prefix, prefix + 1 }) {
            String s = Long.toString(p);
            String rev = new StringBuilder(s).reverse().toString();
            String cand = (length % 2 == 0) ? s + rev : s + rev.substring(1);
            cands.add(Long.parseLong(cand));
        }
        cands.remove(num);

        long best = -1;
        for (long c : cands) {
            if (c < 0) continue;
            if (best == -1 || Math.abs(c - num) < Math.abs(best - num)
                    || (Math.abs(c - num) == Math.abs(best - num) && c < best)) {
                best = c;
            }
        }
        return Long.toString(best);
    }

    private long pow10(int e) {
        long r = 1;
        for (int i = 0; i < e; i++) r *= 10;
        return r;
    }

    public static void main(String[] args) {
        FindTheClosestPalindrome s = new FindTheClosestPalindrome();
        for (String t : new String[] { "123", "1", "10", "1000", "999" }) {
            System.out.println(s.nearestPalindromic(t));  // 121, 0, 9, 999, 1001
        }
    }
}
