class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                result.append(abs(num))

        return result
