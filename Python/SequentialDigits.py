class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for start_digit in range(1, 10):
            num = start_digit
            next_digit = start_digit
            while num <= high and next_digit < 10:
                if num >= low:
                    result.append(num)
                next_digit += 1
                num = num * 10 + next_digit
        return sorted(result)
