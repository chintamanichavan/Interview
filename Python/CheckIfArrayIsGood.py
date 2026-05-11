class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        return sorted(nums) == list(range(1, n + 1)) + [n]
