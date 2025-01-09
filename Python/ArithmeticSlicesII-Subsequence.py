class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        total_count = 0
        dp = [{} for _ in nums]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Count of subsequences ending with nums[j] having difference diff
                count_j = dp[j].get(diff, 0)
                # Count of subsequences ending with nums[i] having difference diff
                count_i = dp[i].get(diff, 0)
                
                # Update the count for nums[i] and difference diff
                dp[i][diff] = count_i + count_j + 1

                # If count_j is at least 1, it contributes to the total count of arithmetic subsequences
                if count_j >= 1:
                    total_count += count_j

        return total_count
