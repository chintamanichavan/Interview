class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # Difference array over possible target sums [2, 2*limit].
        # For each pair (a, b) with a <= b, the moves-vs-target curve is:
        #   target < 1+a        -> 2
        #   1+a <= target < a+b -> 1
        #   target == a+b       -> 0
        #   a+b < target <= b+limit -> 1
        #   target > b+limit    -> 2
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            x, y = nums[i], nums[n - 1 - i]
            a, b = (x, y) if x <= y else (y, x)
            diff[2] += 2
            diff[1 + a] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1

        ans = n
        cur = 0
        for t in range(2, 2 * limit + 1):
            cur += diff[t]
            if cur < ans:
                ans = cur
        return ans
