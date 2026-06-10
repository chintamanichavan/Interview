import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # Both arrays sorted. Seed the heap with (nums1[i] + nums2[0], i, 0) for the first k of
        # nums1; each pop (i, j) pushes its right neighbor (i, j+1). Best-first yields pairs in
        # ascending sum order. O(k log k).
        if not nums1 or not nums2:
            return []
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))  # [[1, 2], [1, 4], [1, 6]]
    print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))  # [[1, 1], [1, 1]]
    print(s.kSmallestPairs([1, 2], [3], 3))  # [[1, 3], [2, 3]]
