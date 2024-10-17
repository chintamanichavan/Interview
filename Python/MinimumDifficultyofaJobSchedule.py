class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        # Initialize the DP table with infinity
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                max_difficulty = 0
                for k in range(i, j - 1, -1):  # Iterate backwards to find the partition
                    max_difficulty = max(max_difficulty, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + max_difficulty)

        return dp[n][d] if dp[n][d] < float('inf') else -1
