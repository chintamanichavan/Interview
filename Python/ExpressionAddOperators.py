class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index, expression, value, prev):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break

                curr = int(num[index:i+1])

                if index == 0:
                    backtrack(i + 1, expression + str(curr), curr, curr)
                else:
                    backtrack(i + 1, expression + '+' + str(curr), value + curr, curr)
                    backtrack(i + 1, expression + '-' + str(curr), value - curr, -curr)
                    backtrack(i + 1, expression + '*' + str(curr), value - prev + prev * curr, prev * curr)

        backtrack(0, '', 0, 0)
        return result
