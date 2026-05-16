class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        ans = [0] * n
        prefix_max = nums[0]
        group_max = nums[0]
        start = 0
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            group_max = max(group_max, nums[i])
            if i == n - 1 or prefix_max <= suffix_min[i + 1]:
                for k in range(start, i + 1):
                    ans[k] = group_max
                start = i + 1
                if i + 1 < n:
                    group_max = nums[i + 1]
        return ans
