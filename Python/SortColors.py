
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

# Example usage:
# sol = Solution()
# nums = [2,0,2,1,1,0]
# sol.sortColors(nums)
# print(nums)  # Output: [0,0,1,1,2,2]

# nums = [2,0,1]
# sol.sortColors(nums)
# print(nums)  # Output: [0,1,2]
