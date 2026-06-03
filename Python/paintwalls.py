from math import inf
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # dp[j] = min cost to get j walls painted. The paid painter takes time[i] units,
        # during which the free painter clears up to time[i] other walls, so wall i covers
        # time[i] + 1 walls. Bounded 0/1 knapsack over walls, capacity n.
        n = len(cost)
        dp = [0] + [inf] * n
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]


def main():
    s = Solution()
    print(s.paintWalls([1, 2, 3, 2], [1, 2, 3, 2]))  # 3
    print(s.paintWalls([2, 3, 4, 2], [1, 1, 1, 1]))  # 4


if __name__ == '__main__':
    main()


# review 2025-09-05
