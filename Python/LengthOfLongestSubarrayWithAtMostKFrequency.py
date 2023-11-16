class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        n = len(nums)
        ans = 0
        i = 0
        j = 0
        while j < n:
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans
