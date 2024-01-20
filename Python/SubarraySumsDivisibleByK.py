from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = defaultdict(int)
        remainder_map[0] = 1  # Initialize with remainder 0 count as 1
        cumulative_sum = 0
        count = 0

        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k

            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k

            if remainder in remainder_map:
                count += remainder_map[remainder]

            remainder_map[remainder] += 1

        return count

# Test cases
sol = Solution()
print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))  # Output: 7
print(sol.subarraysDivByK([5], 9))  # Output: 0
