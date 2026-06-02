import java.util.HashMap;
import java.util.Map;

public class ScrambleString {
    private final Map<String, Boolean> memo = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        return solve(s1, s2);
    }

    private boolean solve(String a, String b) {
        if (a.equals(b)) return true;
        String key = a + "|" + b;
        Boolean cached = memo.get(key);
        if (cached != null) return cached;

        int[] cnt = new int[26];
        for (int i = 0; i < a.length(); i++) {
            cnt[a.charAt(i) - 'a']++;
            cnt[b.charAt(i) - 'a']--;
        }
        for (int c : cnt) {
            if (c != 0) {
                memo.put(key, false);
                return false;
            }
        }
        int n = a.length();
        for (int i = 1; i < n; i++) {
            if (solve(a.substring(0, i), b.substring(0, i)) && solve(a.substring(i), b.substring(i))) {
                memo.put(key, true);
                return true;
            }
            if (solve(a.substring(0, i), b.substring(n - i)) && solve(a.substring(i), b.substring(0, n - i))) {
                memo.put(key, true);
                return true;
            }
        }
        memo.put(key, false);
        return false;
    }

    public static void main(String[] args) {
        ScrambleString s = new ScrambleString();
        System.out.println(s.isScramble("great", "rgeat")); // true
        System.out.println(s.isScramble("abcde", "caebd")); // false
        System.out.println(s.isScramble("a", "a"));         // true
        System.out.println(s.isScramble("abc", "bca"));     // true
    }
}
