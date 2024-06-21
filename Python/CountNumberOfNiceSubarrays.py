
from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Step 1: Convert nums to a binary array where 1 represents an odd number and 0 represents an even number
        binary_nums = [1 if num % 2 != 0 else 0 for num in nums]

        # Step 2: Initialize prefix sum and hashmap to store the frequency of prefix sums
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # To handle the case when the subarray starts from index 0

        count_nice_subarrays = 0

        # Step 3: Traverse through the binary array
        for num in binary_nums:
            prefix_sum += num
            # If (prefix_sum - k) exists in prefix_count, it means there are subarrays ending at the current index with exactly k odd numbers
            count_nice_subarrays += prefix_count[prefix_sum - k]
            # Update the prefix_count with the current prefix_sum
            prefix_count[prefix_sum] += 1

        return count_nice_subarrays

# Example usage:
sol = Solution()
print(sol.numberOfSubarrays([1, 1, 2, 1, 1], 3))  # Output: 2
print(sol.numberOfSubarrays([2, 4, 6], 1))        # Output: 0
print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # Output: 16
