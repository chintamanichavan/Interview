from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 0/1 knapsack on (members, profit_capped_at_minProfit). dp[j][k] = # schemes using
        # exactly j members with profit floored at min(actual, minProfit) = k.
        # Iterate j and k in reverse so each crime is counted at most once.
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for j in range(n, g - 1, -1):
                for k in range(minProfit, -1, -1):
                    if dp[j - g][k]:
                        nk = min(minProfit, k + p)
                        dp[j][nk] = (dp[j][nk] + dp[j - g][k]) % MOD
        return sum(dp[j][minProfit] for j in range(n + 1)) % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.profitableSchemes(5, 3, [2, 2], [2, 3]))         # 2
    print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))  # 7
    print(s.profitableSchemes(1, 1, [1, 1], [1, 1]))         # 2
    # Sum of profits = 78 < minProfit=100, so 0 valid schemes.
    print(s.profitableSchemes(100, 100, [2, 5, 36, 2, 5, 5, 14, 1, 12, 1, 14, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # 0
