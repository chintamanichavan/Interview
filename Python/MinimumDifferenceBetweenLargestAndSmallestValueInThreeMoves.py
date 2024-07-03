
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()

        # We have four scenarios to consider
        # Change the three smallest
        # Change the two smallest and one largest
        # Change the smallest and two largest
        # Change the three largest

        # Minimize the difference between the largest and smallest value after three moves
        return min(
            nums[-1] - nums[3],  # Changing the three smallest
            nums[-2] - nums[2],  # Changing the smallest and two largest
            nums[-3] - nums[1],  # Changing the two smallest and one largest
            nums[-4] - nums[0]   # Changing the three largest
        )

# Example usage:
solution = Solution()
print(solution.minDifference([5, 3, 2, 4]))         # Output: 0
print(solution.minDifference([1, 5, 0, 10, 14]))    # Output: 1
print(solution.minDifference([3, 100, 20]))         # Output: 0
