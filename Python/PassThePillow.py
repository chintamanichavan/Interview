#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Determine the number of full back-and-forth cycles
        cycle_length = (n - 1) * 2
        full_cycles = time // cycle_length

        # Determine the position within the current cycle
        remaining_time = time % cycle_length

        if remaining_time < n:
            # The pillow is moving forward
            return remaining_time + 1
        else:
            # The pillow is moving backward
            return n - (remaining_time - (n - 1))

# Example usage:
sol = Solution()
print(sol.passThePillow(4, 5))  # Output: 2
print(sol.passThePillow(3, 2))  # Output: 3
        
# @lc code=end

