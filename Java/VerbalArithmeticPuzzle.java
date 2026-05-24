import java.util.Arrays;

public class VerbalArithmeticPuzzle {
    private String[] revWords;
    private String revResult;
    private boolean[] leading;
    private int[] charDigit;
    private boolean[] used;

    public boolean isSolvable(String[] words, String result) {
        int maxLen = 0;
        for (String w : words) maxLen = Math.max(maxLen, w.length());
        if (maxLen > result.length()) return false;

        revWords = new String[words.length];
        for (int i = 0; i < words.length; i++) revWords[i] = new StringBuilder(words[i]).reverse().toString();
        revResult = new StringBuilder(result).reverse().toString();

        leading = new boolean[26];
        for (String w : words) if (w.length() > 1) leading[w.charAt(0) - 'A'] = true;
        if (result.length() > 1) leading[result.charAt(0) - 'A'] = true;

        charDigit = new int[26];
        Arrays.fill(charDigit, -1);
        used = new boolean[10];
        return dfs(0, 0, 0);
    }

    private boolean dfs(int col, int idx, int carry) {
        if (col == revResult.length()) return carry == 0;
        if (idx < revWords.length) {
            String w = revWords[idx];
            if (col >= w.length() || charDigit[w.charAt(col) - 'A'] != -1) {
                return dfs(col, idx + 1, carry);
            }
            int ch = w.charAt(col) - 'A';
            for (int d = 0; d < 10; d++) {
                if (used[d] || (d == 0 && leading[ch])) continue;
                charDigit[ch] = d;
                used[d] = true;
                if (dfs(col, idx + 1, carry)) return true;
                charDigit[ch] = -1;
                used[d] = false;
            }
            return false;
        }

        int colSum = carry;
        for (String w : revWords) {
            if (col < w.length()) colSum += charDigit[w.charAt(col) - 'A'];
        }
        int digit = colSum % 10, nextCarry = colSum / 10;
        int rCh = revResult.charAt(col) - 'A';
        if (charDigit[rCh] != -1) {
            if (charDigit[rCh] != digit) return false;
            return dfs(col + 1, 0, nextCarry);
        }
        if (used[digit] || (digit == 0 && leading[rCh])) return false;
        charDigit[rCh] = digit;
        used[digit] = true;
        if (dfs(col + 1, 0, nextCarry)) return true;
        charDigit[rCh] = -1;
        used[digit] = false;
        return false;
    }

    public static void main(String[] args) {
        VerbalArithmeticPuzzle s = new VerbalArithmeticPuzzle();
        System.out.println(s.isSolvable(new String[] { "SEND", "MORE" }, "MONEY"));            // true
        System.out.println(s.isSolvable(new String[] { "SIX", "SEVEN", "SEVEN" }, "TWENTY")); // true
        System.out.println(s.isSolvable(new String[] { "LEET", "CODE" }, "POINT"));            // false
        System.out.println(s.isSolvable(new String[] { "A", "B" }, "C"));                      // true
        System.out.println(s.isSolvable(new String[] { "ACA" }, "JA"));                        // false
    }
}
