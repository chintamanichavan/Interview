from typing import Dict, List


class Solution:
    def evaluate(self, expression: str) -> int:
        # Recursive evaluator with lexical scope. scope maps var -> stack of values (inner shadows
        # outer). An expression is an int literal, a variable, or (let ...) / (add a b) / (mult a b).
        # let binds pairs then evaluates its final body; bindings are popped on exit to restore scope.
        scope: Dict[str, List[int]] = {}

        def tokens(s: str) -> List[str]:
            # split the body of a (...) form into top-level tokens, respecting nested parens
            res, depth, cur = [], 0, []
            for ch in s:
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                if ch == " " and depth == 0:
                    if cur:
                        res.append("".join(cur))
                        cur = []
                else:
                    cur.append(ch)
            if cur:
                res.append("".join(cur))
            return res

        def ev(expr: str) -> int:
            if expr[0] != "(":
                if expr.lstrip("-").isdigit():
                    return int(expr)
                return scope[expr][-1]

            inner = expr[1:-1]
            parts = tokens(inner)
            op = parts[0]
            if op == "add":
                return ev(parts[1]) + ev(parts[2])
            if op == "mult":
                return ev(parts[1]) * ev(parts[2])
            # let: pairs of (var, value), then a final body expression
            assigned = []
            i = 1
            while i + 1 < len(parts):
                var = parts[i]
                val = ev(parts[i + 1])
                scope.setdefault(var, []).append(val)
                assigned.append(var)
                i += 2
            result = ev(parts[i])
            for var in assigned:
                scope[var].pop()
            return result

        return ev(expression)


if __name__ == "__main__":
    s = Solution()
    print(s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))  # 14
    print(s.evaluate("(let x 3 x 2 x)"))  # 2
    print(s.evaluate("(let x 1 y 2 x (add x y) (add x y))"))  # 5
    print(s.evaluate("(add 1 2)"))  # 3
    print(s.evaluate("(let x 7 -12)"))  # -12
