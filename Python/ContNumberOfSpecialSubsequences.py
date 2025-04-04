
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count_0, count_1, count_2 = 0, 0, 0

        for num in nums:
            if num == 0:
                count_0 = (2 * count_0 + 1) % MOD
            elif num == 1:
                count_1 = (2 * count_1 + count_0) % MOD
            elif num == 2:
                count_2 = (2 * count_2 + count_1) % MOD

        return count_2

