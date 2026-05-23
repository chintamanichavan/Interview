import java.util.HashMap;
import java.util.Map;

public class CouplesHoldingHands {
    public int minSwapsCouples(int[] row) {
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < row.length; i++) pos.put(row[i], i);
        int swaps = 0;
        for (int i = 0; i < row.length; i += 2) {
            int partner = row[i] ^ 1;
            if (row[i + 1] == partner) continue;
            int j = pos.get(partner);
            int tmp = row[i + 1];
            row[i + 1] = row[j];
            row[j] = tmp;
            pos.put(row[j], j);
            pos.put(row[i + 1], i + 1);
            swaps++;
        }
        return swaps;
    }

    public static void main(String[] args) {
        CouplesHoldingHands s = new CouplesHoldingHands();
        System.out.println(s.minSwapsCouples(new int[] { 0, 2, 1, 3 }));            // 1
        System.out.println(s.minSwapsCouples(new int[] { 3, 2, 0, 1 }));            // 0
        System.out.println(s.minSwapsCouples(new int[] { 0, 2, 4, 1, 3, 5 }));      // 2
        System.out.println(s.minSwapsCouples(new int[] { 5, 4, 2, 6, 3, 1, 0, 7 })); // 2
    }
}
