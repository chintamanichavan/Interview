class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        result = []
        n = len(nums)

        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] <= k:
                result.append(nums[i:i + 3])
            else:
                return []  # Impossible to satisfy the conditions

        return result
