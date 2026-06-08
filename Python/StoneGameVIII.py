from itertools import accumulate
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Every move = choose split i (>=1) and score prefix[i]; the opponent then plays on
        # splits > i. dp[i] = best score difference for the player to move when the smallest
        # allowed split is i: dp[i] = max(dp[i+1], prefix[i] - dp[i+1]). Answer = dp[1].
        prefix = list(accumulate(stones))
        n = len(stones)
        dp = prefix[n - 1]  # forced to take everything at the last split
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGameVIII([-1, 2, -3, 4, -5]))           # 5
    print(s.stoneGameVIII([7, -6, 5, 10, 5, -2, -6]))    # 13
    print(s.stoneGameVIII([-10, -12]))                   # -22
