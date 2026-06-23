import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.StringJoiner;

public class LFUCache {
    private final int cap;
    private int minFreq;
    private final Map<Integer, Integer> keyVal = new HashMap<>();
    private final Map<Integer, Integer> keyFreq = new HashMap<>();
    private final Map<Integer, LinkedHashSet<Integer>> freqKeys = new HashMap<>();  // insertion-ordered

    public LFUCache(int capacity) {
        cap = capacity;
        minFreq = 0;
    }

    public int get(int key) {
        if (!keyVal.containsKey(key)) return -1;
        bump(key);
        return keyVal.get(key);
    }

    public void put(int key, int value) {
        if (cap <= 0) return;
        if (keyVal.containsKey(key)) {
            keyVal.put(key, value);
            bump(key);
            return;
        }
        if (keyVal.size() >= cap) {
            LinkedHashSet<Integer> set = freqKeys.get(minFreq);
            int ek = set.iterator().next();
            set.remove(ek);
            keyVal.remove(ek);
            keyFreq.remove(ek);
        }
        keyVal.put(key, value);
        keyFreq.put(key, 1);
        freqKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
        minFreq = 1;
    }

    private void bump(int key) {
        int f = keyFreq.get(key);
        LinkedHashSet<Integer> set = freqKeys.get(f);
        set.remove(key);
        if (set.isEmpty()) {
            freqKeys.remove(f);
            if (minFreq == f) minFreq++;
        }
        keyFreq.put(key, f + 1);
        freqKeys.computeIfAbsent(f + 1, k -> new LinkedHashSet<>()).add(key);
    }

    public static void main(String[] args) {
        String[] ops = { "LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get" };
        int[][] arg = { {2}, {1, 1}, {2, 2}, {1}, {3, 3}, {2}, {3}, {4, 4}, {1}, {3}, {4} };
        LFUCache c = null;
        StringJoiner sj = new StringJoiner(", ", "[", "]");
        for (int i = 0; i < ops.length; i++) {
            switch (ops[i]) {
                case "LFUCache" -> { c = new LFUCache(arg[i][0]); sj.add("null"); }
                case "get" -> sj.add(Integer.toString(c.get(arg[i][0])));
                case "put" -> { c.put(arg[i][0], arg[i][1]); sj.add("null"); }
            }
        }
        System.out.println(sj);
    }
}
