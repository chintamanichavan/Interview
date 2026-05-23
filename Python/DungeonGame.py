from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # DP from bottom-right back to top-left. dp[j] = min health needed when entering (i, j).
        # need = min(right, below) - dungeon[i][j]; clamp to >= 1 (knight must stay alive).
        # Pre-seed dp[n-1] = 1 so the destination's "below" defaults to 1; everything else INF.
        m, n = len(dungeon), len(dungeon[0])
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[j], dp[j + 1]) - dungeon[i][j]
                dp[j] = max(1, need)
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # 7
    print(s.calculateMinimumHP([[0]]))                                       # 1
    print(s.calculateMinimumHP([[100]]))                                     # 1
    print(s.calculateMinimumHP([[-3]]))                                      # 4
