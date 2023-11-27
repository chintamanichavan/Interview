class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD = 10**9 + 7
        if n == 1:
            return 10

        # Moves from each key
        moves = {
            0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
            4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6],
            8: [1, 3], 9: [2, 4]
        }

        # Dynamic Programming array
        dp = [[0] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(10):
                dp[i][j] = sum(dp[i - 1][k] for k in moves[j]) % MOD

        return sum(dp[-1]) % MOD
