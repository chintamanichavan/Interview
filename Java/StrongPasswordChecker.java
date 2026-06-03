public class StrongPasswordChecker {
    public int strongPasswordChecker(String password) {
        int n = password.length();
        boolean hasLower = false, hasUpper = false, hasDigit = false;
        for (int i = 0; i < n; i++) {
            char c = password.charAt(i);
            if (Character.isLowerCase(c)) hasLower = true;
            else if (Character.isUpperCase(c)) hasUpper = true;
            else if (Character.isDigit(c)) hasDigit = true;
        }
        int missingType = 3 - (hasLower ? 1 : 0) - (hasUpper ? 1 : 0) - (hasDigit ? 1 : 0);

        // Runs of >= 3 equal chars: L/3 replacements; bucket by L%3 for the >20 deletion case.
        int change = 0, one = 0, two = 0;
        int i = 2;
        while (i < n) {
            if (password.charAt(i) == password.charAt(i - 1)
                    && password.charAt(i - 1) == password.charAt(i - 2)) {
                int length = 2;
                while (i < n && password.charAt(i) == password.charAt(i - 1)) { length++; i++; }
                change += length / 3;
                if (length % 3 == 0) one++;
                else if (length % 3 == 1) two++;
            } else {
                i++;
            }
        }

        if (n < 6) return Math.max(6 - n, missingType);
        if (n <= 20) return Math.max(change, missingType);

        int del = n - 20;
        change -= Math.min(del, one);
        change -= Math.min(Math.max(del - one, 0), two * 2) / 2;
        change -= Math.max(del - one - two * 2, 0) / 3;
        return del + Math.max(change, missingType);
    }

    public static void main(String[] args) {
        StrongPasswordChecker s = new StrongPasswordChecker();
        System.out.println(s.strongPasswordChecker("a"));                         // 5
        System.out.println(s.strongPasswordChecker("aA1"));                       // 3
        System.out.println(s.strongPasswordChecker("1337C0d3"));                  // 0
        System.out.println(s.strongPasswordChecker("aaa123"));                    // 1
        System.out.println(s.strongPasswordChecker("aaaaa"));                     // 2
        System.out.println(s.strongPasswordChecker("1111111111"));               // 3
        System.out.println(s.strongPasswordChecker("aaaabbaaabbaaabbaaabbaaaa")); // 7
    }
}
