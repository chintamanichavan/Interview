from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Greedy: sort ascending and consume in order. If the smallest remaining asteroid
        # exceeds current mass, no ordering can help (later asteroids are at least as large).
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))  # True
    print(s.asteroidsDestroyed(5, [4, 9, 23, 4]))       # False
    print(s.asteroidsDestroyed(1, [1]))                 # True
    print(s.asteroidsDestroyed(1, [2]))                 # False
