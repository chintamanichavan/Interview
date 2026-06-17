from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary search on the answer (the largest subarray sum). The minimum feasible cap lies
        # in [max(nums), sum(nums)]; a cap is feasible if greedily packing subarrays needs <= k
        # of them. Feasibility is monotone in the cap, so binary search applies. O(n log sum).
        def needed(cap: int) -> int:
            count, cur = 1, 0
            for x in nums:
                if cur + x > cap:
                    count += 1
                    cur = x
                else:
                    cur += x
            return count

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if needed(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))  # 18
    print(s.splitArray([1, 2, 3, 4, 5], 2))  # 9
    print(s.splitArray([1, 4, 4], 3))  # 4
