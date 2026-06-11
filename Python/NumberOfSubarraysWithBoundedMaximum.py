from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # count(b) = # subarrays whose every element is <= b (a running length of consecutive
        # in-bound elements contributes len subarrays ending here). Subarrays with max in
        # [left, right] = count(right) - count(left - 1). O(n).
        def count(bound: int) -> int:
            total = 0
            length = 0
            for x in nums:
                length = length + 1 if x <= bound else 0
                total += length
            return total

        return count(right) - count(left - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))  # 3
    print(s.numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8))  # 7
    print(s.numSubarrayBoundedMax([1, 1, 1], 1, 1))  # 6
