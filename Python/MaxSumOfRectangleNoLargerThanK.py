import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Fix a pair of columns [left, right] and compress each row to its sum across those
        # columns -> a 1D array. The best subarray sum <= k in that 1D array is found with an
        # ordered set of prefix sums: for running prefix `cur`, the smallest stored prefix
        # >= cur - k gives the largest subarray sum <= k ending here. O(cols^2 * rows log rows).
        m, n = len(matrix), len(matrix[0])
        best = float("-inf")
        for left in range(n):
            rowsum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowsum[i] += matrix[i][right]
                prefixes = [0]
                cur = 0
                for v in rowsum:
                    cur += v
                    idx = bisect.bisect_left(prefixes, cur - k)
                    if idx < len(prefixes):
                        best = max(best, cur - prefixes[idx])
                    bisect.insort(prefixes, cur)
        return best


if __name__ == "__main__":
    s = Solution()
    print(s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))  # 2
    print(s.maxSumSubmatrix([[2, 2, -1]], 3))  # 3
    print(s.maxSumSubmatrix([[2, 2, -1]], 0))  # -1
