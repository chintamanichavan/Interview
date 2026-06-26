from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Backtracking: repeatedly pick any two values, combine them with +, -, *, / (both orders
        # for - and /), and recurse on the reduced multiset until one value remains. Use a small
        # epsilon for the float comparison. Only 4 cards, so the search is tiny.
        EPS = 1e-6

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    rest = [nums[x] for x in range(n) if x != i and x != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    for val in candidates:
                        if solve(rest + [val]):
                            return True
            return False

        return solve([float(c) for c in cards])


if __name__ == "__main__":
    s = Solution()
    print(s.judgePoint24([4, 1, 8, 7]))  # True
    print(s.judgePoint24([1, 2, 1, 2]))  # False
    print(s.judgePoint24([3, 3, 8, 8]))  # True  (8/(3-8/3))
    print(s.judgePoint24([1, 1, 1, 1]))  # False
