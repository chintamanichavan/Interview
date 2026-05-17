from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = [False] * n
        queue = deque([start])
        seen[start] = True
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            for j in (i + arr[i], i - arr[i]):
                if 0 <= j < n and not seen[j]:
                    seen[j] = True
                    queue.append(j)
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canReach([4, 2, 3, 0, 3, 1, 2], 5))  # True
    print(s.canReach([4, 2, 3, 0, 3, 1, 2], 0))  # True
    print(s.canReach([3, 0, 2, 1, 2], 2))        # False
