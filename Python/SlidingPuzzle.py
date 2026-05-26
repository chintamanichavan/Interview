from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # BFS over board states encoded as 6-char strings. Adjacency is fixed for a 2x3 grid:
        # positions 0..5 flatten to (0 1 2 / 3 4 5).
        neighbors = [(1, 3), (0, 2, 4), (1, 5),
                     (0, 4),    (1, 3, 5), (2, 4)]
        start = ''.join(str(c) for row in board for c in row)
        target = '123450'
        if start == target:
            return 0

        queue = deque([(start, start.index('0'), 0)])
        seen = {start}
        while queue:
            state, zero, steps = queue.popleft()
            for nb in neighbors[zero]:
                lst = list(state)
                lst[zero], lst[nb] = lst[nb], lst[zero]
                nxt = ''.join(lst)
                if nxt == target:
                    return steps + 1
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, nb, steps + 1))
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))  # 1
    print(s.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))  # -1
    print(s.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))  # 5
    print(s.slidingPuzzle([[1, 2, 3], [4, 5, 0]]))  # 0
