class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            best = -1
            for j in range(i):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    if dp[j] + 1 > best:
                        best = dp[j] + 1
            dp[i] = best
        return dp[n - 1]
