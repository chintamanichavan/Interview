class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        sum = 0
        sumMap = {0: -1}  # Initialize the sum map with a sum of 0 at index -1

        for i in range(len(nums)):
            sum += -1 if nums[i] == 0 else 1  # Increment sum by -1 for 0 and 1 for 1

            if sum in sumMap:
                maxLen = max(maxLen, i - sumMap[sum])  # Update maxLen if necessary
            else:
                sumMap[sum] = i  # Store the first occurrence of the sum

        return maxLen
