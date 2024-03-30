class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)

    def atMostKDistinct(self, nums, k):
        n = len(nums)
        freq = [0] * (n + 1)
        distinct = 0
        left = 0
        count = 0

        for right in range(n):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            count += right - left + 1

        return count
