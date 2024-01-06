import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted(zip(endTime, startTime, profit))
        dp = [(0, 0)]  # (endTime, totalProfit) pair

        for end, start, profit in jobs:
            # Binary search for the last job that doesn't overlap with the current job
            i = bisect.bisect(dp, (start, float('inf'))) - 1
            if dp[i][1] + profit > dp[-1][1]:
                # If including the current job leads to a higher profit, update the dp array
                dp.append((end, dp[i][1] + profit))

        return dp[-1][1]
