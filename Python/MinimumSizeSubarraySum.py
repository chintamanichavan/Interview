from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        min_len = inf

        for right in range(n):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == inf else min_len


def main():
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))         # 2
    print(s.minSubArrayLen(4, [1, 4, 4]))                  # 1
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0


if __name__ == '__main__':
    main()


# review 2024-02-12

# review 2024-05-11
