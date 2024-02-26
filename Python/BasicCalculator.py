class Solution():
    def calculate(self, s):
        def evaluate(expression):
            stack = []
            num = 0
            operator = '+'

            while expression:
                ch = expression.pop(0)

                if ch.isdigit():
                    num = num * 10 + int(ch)

                if (not ch.isdigit() and ch != ' ') or len(expression) == 0:
                    if operator == '+':
                        stack.append(num)
                    elif operator == '-':
                        stack.append(-num)
                    operator = ch
                    num = 0

                if ch == '(':
                    num = evaluate(expression[:])  # Pass a copy of expression

                if ch == ')':
                    # Apply the operator before the opening parenthesis to the entire sub-expression
                    while stack and isinstance(stack[-1], int):
                        num = stack.pop() + num if stack[-1] == '+' else stack.pop() - num
                    break

            return sum(stack)

        return evaluate(list(s))

def main():
    s = "(1+(4+5+2)-3)+(6+8)"
    sol = Solution()
    res = sol.calculate(s)
    print(res)

if __name__ == '__main__':
    main()
