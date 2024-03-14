class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        sum_count = {0: 1}  # Initialize sum 0 with count 1

        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num

            if current_sum - goal in sum_count:
                count += sum_count[current_sum - goal]

            sum_count[current_sum] = sum_count.get(current_sum, 0) + 1

        return count
