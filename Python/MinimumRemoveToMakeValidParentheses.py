class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: remove invalid closing parentheses
        stack = []
        s = list(s)
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        # Second pass: remove invalid opening parentheses
        while stack:
            s[stack.pop()] = ''

        return ''.join(s)
