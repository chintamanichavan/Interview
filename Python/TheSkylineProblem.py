import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sweep line + max-heap. Events: (x, -h, r) for starts, (r, 0, 0) as sweep markers
        # at end-x. Sorting puts starts (neg h) before ends (h=0) at the same x, and within
        # starts the taller comes first — both required for correct merging at building edges.
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        result: List[List[int]] = []
        heap = [(0, float('inf'))]  # (-height, end_x); sentinel ground keeps heap non-empty

        for x, neg_h, r in events:
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))
            while heap[0][1] <= x:  # lazy-delete expired buildings
                heapq.heappop(heap)
            cur_max = -heap[0][0]
            if not result or result[-1][1] != cur_max:
                result.append([x, cur_max])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    print(s.getSkyline([[0, 2, 3], [2, 5, 3]]))         # [[0,3],[5,0]]
    print(s.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))  # [[1,3],[2,0]]
    print(s.getSkyline([[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]])) # [[0,3],[7,0]]
