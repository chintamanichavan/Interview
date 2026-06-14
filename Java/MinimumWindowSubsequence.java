public class MinimumWindowSubsequence {
    public String minWindow(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int i = 0, j = 0, start = -1, best = m + 1;
        while (i < m) {
            if (s1.charAt(i) == s2.charAt(j)) {
                if (++j == n) {
                    int right = i;
                    --j;
                    while (j >= 0) {
                        if (s1.charAt(i) == s2.charAt(j)) --j;
                        --i;
                    }
                    ++i;  // left end
                    if (right - i + 1 < best) {
                        best = right - i + 1;
                        start = i;
                    }
                    j = 0;
                }
            }
            ++i;
        }
        return start == -1 ? "" : s1.substring(start, start + best);
    }

    public static void main(String[] args) {
        MinimumWindowSubsequence s = new MinimumWindowSubsequence();
        System.out.println(s.minWindow("abcdebdde", "bde"));  // bcde
        System.out.println(s.minWindow("abc", "ac"));         // abc
        System.out.println(s.minWindow("abcde", "xyz"));      // (empty)
    }
}
