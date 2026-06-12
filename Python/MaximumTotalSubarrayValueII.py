import heapq
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # value(l, r) = max(nums[l..r]) - min(nums[l..r]) is monotone: shrinking a subarray
        # can only reduce it, so [0, n-1] is the global maximum and every subarray is reached
        # from it by shrinking. Best-first pop the largest, push children [l+1,r] and [l,r-1].
        # Sparse tables give O(1) range max/min.
        n = len(nums)

        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        up_max = [nums[:]]
        up_min = [nums[:]]
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            length = 1 << j
            pmx, pmn = up_max[j - 1], up_min[j - 1]
            cmx = [0] * (n - length + 1)
            cmn = [0] * (n - length + 1)
            for i in range(n - length + 1):
                cmx[i] = max(pmx[i], pmx[i + half])
                cmn[i] = min(pmn[i], pmn[i + half])
            up_max.append(cmx)
            up_min.append(cmn)
            j += 1

        def value(l: int, r: int) -> int:
            j = log[r - l + 1]
            shift = 1 << j
            mx = max(up_max[j][l], up_max[j][r - shift + 1])
            mn = min(up_min[j][l], up_min[j][r - shift + 1])
            return mx - mn

        heap = [(-value(0, n - 1), 0, n - 1)]
        seen = {(0, n - 1)}
        total = 0
        for _ in range(k):
            neg, l, r = heapq.heappop(heap)
            total += -neg
            if l + 1 <= r and (l + 1, r) not in seen:
                seen.add((l + 1, r))
                heapq.heappush(heap, (-value(l + 1, r), l + 1, r))
            if l <= r - 1 and (l, r - 1) not in seen:
                seen.add((l, r - 1))
                heapq.heappush(heap, (-value(l, r - 1), l, r - 1))
        return total


if __name__ == "__main__":
    s = Solution()
    print(s.maxTotalValue([1, 3, 2], 2))  # 4
    print(s.maxTotalValue([4, 2, 5, 1], 3))  # 12
    print(s.maxTotalValue([1], 1))  # 0
