public class DecodeWaysII {
    private static final long MOD = 1_000_000_007L;

    public int numDecodings(String s) {
        long prev2 = 1, prev1 = one(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            long cur = (one(s.charAt(i)) * prev1 + two(s.charAt(i - 1), s.charAt(i)) * prev2) % MOD;
            prev2 = prev1;
            prev1 = cur;
        }
        return (int) (prev1 % MOD);
    }

    private static int one(char c) {
        if (c == '*') return 9;
        if (c == '0') return 0;
        return 1;
    }

    private static int two(char c1, char c2) {
        if (c1 == '1') return (c2 == '*') ? 9 : 1;
        if (c1 == '2') {
            if (c2 == '*') return 6;
            return (c2 >= '0' && c2 <= '6') ? 1 : 0;
        }
        if (c1 == '*') {
            if (c2 == '*') return 15;
            if (c2 >= '0' && c2 <= '6') return 2;
            return 1;
        }
        return 0;
    }

    public static void main(String[] args) {
        DecodeWaysII s = new DecodeWaysII();
        System.out.println(s.numDecodings("*"));  // 9
        System.out.println(s.numDecodings("1*")); // 18
        System.out.println(s.numDecodings("2*")); // 15
        System.out.println(s.numDecodings("0"));  // 0
        System.out.println(s.numDecodings("**")); // 96
        System.out.println(s.numDecodings("*1")); // 11
    }
}
