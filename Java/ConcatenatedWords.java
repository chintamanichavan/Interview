import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ConcatenatedWords {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> set = new HashSet<>();
        for (String w : words) set.add(w);
        List<String> res = new ArrayList<>();
        for (String w : words) {
            if (!w.isEmpty() && canForm(w, set)) res.add(w);
        }
        return res;
    }

    private boolean canForm(String word, Set<String> set) {
        int n = word.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (!dp[j] || (j == 0 && i == n)) continue;
                if (set.contains(word.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        ConcatenatedWords s = new ConcatenatedWords();
        System.out.println(s.findAllConcatenatedWordsInADict(new String[] { "cat", "cats", "catsdogcats",
                "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat" }));
        System.out.println(s.findAllConcatenatedWordsInADict(new String[] { "cat", "dog", "catdog" }));
        System.out.println(s.findAllConcatenatedWordsInADict(new String[] { "a", "b", "ab", "abc" }));
    }
}
