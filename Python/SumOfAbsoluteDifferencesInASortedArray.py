class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        # Calculate prefix sums
        prefix_sum = 0
        for i in range(n):
            result[i] = nums[i] * i - prefix_sum
            prefix_sum += nums[i]

        # Calculate suffix sums and add to result
        suffix_sum = 0
        for i in range(n - 1, -1, -1):
            result[i] += suffix_sum - nums[i] * (n - 1 - i)
            suffix_sum += nums[i]

        return result
