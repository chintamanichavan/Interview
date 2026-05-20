from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        # Pigeonhole: with n numbers in [mn, mx], the max gap is >= ceil((mx-mn)/(n-1)),
        # so it must occur between buckets of that size, not within one.
        bucket_size = max(1, (mx - mn) // (n - 1))
        num_buckets = (mx - mn) // bucket_size + 1
        bucket_min = [None] * num_buckets
        bucket_max = [None] * num_buckets

        for x in nums:
            i = (x - mn) // bucket_size
            bucket_min[i] = x if bucket_min[i] is None else min(bucket_min[i], x)
            bucket_max[i] = x if bucket_max[i] is None else max(bucket_max[i], x)

        best = 0
        prev_max = mn
        for i in range(num_buckets):
            if bucket_min[i] is None:
                continue
            best = max(best, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        return best


if __name__ == '__main__':
    s = Solution()
    print(s.maximumGap([3, 6, 9, 1]))  # 3
    print(s.maximumGap([10]))          # 0
    print(s.maximumGap([1, 1, 1, 1]))  # 0
    print(s.maximumGap([1, 10000000])) # 9999999
