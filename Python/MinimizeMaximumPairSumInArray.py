class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        # Sort the array to pair the largest with the smallest element.
        nums.sort()

        # Initialize a variable to store the minimized maximum pair sum.
        min_max_pair_sum = 0

        # Iterate over the array in steps of 2 and calculate the pair sums.
        for i in range(0, len(nums), 2):
            pair_sum = nums[i] + nums[-(i+1)]
            # Update the minimized maximum pair sum if the current pair sum is larger.
            min_max_pair_sum = max(min_max_pair_sum, pair_sum)

        return min_max_pair_sum
