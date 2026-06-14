import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # K-way merge: keep one pointer per list in a min-heap and track the current max across
        # the heap. The window [heap-min, cur-max] covers one element from every list; advance the
        # list owning the min and update. The smallest such window over the merge is the answer.
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        cur_max = max(row[0] for row in nums)
        best = [heap[0][0], cur_max]
        while True:
            val, i, j = heapq.heappop(heap)
            if cur_max - val < best[1] - best[0]:
                best = [val, cur_max]
            if j + 1 == len(nums[i]):
                break  # this list is exhausted; no further window can cover it
            nxt = nums[i][j + 1]
            cur_max = max(cur_max, nxt)
            heapq.heappush(heap, (nxt, i, j + 1))
        return best


if __name__ == "__main__":
    s = Solution()
    print(
        s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    )  # [20, 24]
    print(s.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))  # [1, 1]
    print(s.smallestRange([[1], [2], [3]]))  # [1, 3]
