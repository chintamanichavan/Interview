class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0: -1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %= k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >= 2:
                return True
        return False

# review 2025-08-06

# review 2025-10-20

# review 2026-03-21
