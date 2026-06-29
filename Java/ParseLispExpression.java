import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParseLispExpression {
    private final Map<String, Deque<Integer>> scope = new HashMap<>();

    public int evaluate(String expression) {
        return ev(expression);
    }

    private List<String> topTokens(String s) {
        List<String> res = new ArrayList<>();
        int depth = 0;
        StringBuilder cur = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (ch == '(') depth++;
            else if (ch == ')') depth--;
            if (ch == ' ' && depth == 0) {
                if (cur.length() > 0) { res.add(cur.toString()); cur.setLength(0); }
            } else {
                cur.append(ch);
            }
        }
        if (cur.length() > 0) res.add(cur.toString());
        return res;
    }

    private boolean isIntLiteral(String s) {
        if (s.isEmpty()) return false;
        int i = (s.charAt(0) == '-') ? 1 : 0;
        if (i == s.length()) return false;
        for (; i < s.length(); i++) if (!Character.isDigit(s.charAt(i))) return false;
        return true;
    }

    private int ev(String expr) {
        if (expr.charAt(0) != '(') {
            if (isIntLiteral(expr)) return Integer.parseInt(expr);
            return scope.get(expr).peek();
        }
        List<String> parts = topTokens(expr.substring(1, expr.length() - 1));
        if (parts.get(0).equals("add")) return ev(parts.get(1)) + ev(parts.get(2));
        if (parts.get(0).equals("mult")) return ev(parts.get(1)) * ev(parts.get(2));
        // let
        List<String> assigned = new ArrayList<>();
        int i = 1;
        while (i + 1 < parts.size()) {
            int val = ev(parts.get(i + 1));
            scope.computeIfAbsent(parts.get(i), k -> new ArrayDeque<>()).push(val);
            assigned.add(parts.get(i));
            i += 2;
        }
        int result = ev(parts.get(i));
        for (String v : assigned) scope.get(v).pop();
        return result;
    }

    public static void main(String[] args) {
        ParseLispExpression s = new ParseLispExpression();
        System.out.println(s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"));  // 14
        System.out.println(s.evaluate("(let x 3 x 2 x)"));                             // 2
        System.out.println(s.evaluate("(let x 1 y 2 x (add x y) (add x y))"));         // 5
        System.out.println(s.evaluate("(add 1 2)"));                                   // 3
        System.out.println(s.evaluate("(let x 7 -12)"));                               // -12
    }
}
