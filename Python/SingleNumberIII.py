class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all the numbers to get xor_result
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Step 2: Find a set bit in xor_result (we use the rightmost set bit)
        rightmost_set_bit = xor_result & -xor_result

        # Step 3: Divide the numbers into two groups and XOR them separately
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

# Example usage:
# sol = Solution()
# print(sol.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3, 5] or [5, 3]
# print(sol.singleNumber([-1, 0]))  # Output: [-1, 0] or [0, -1]
# print(sol.singleNumber([0, 1]))  # Output: [1, 0] or [0, 1]
