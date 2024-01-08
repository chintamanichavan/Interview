class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Sort the array in descending order
        nums.sort(reverse=True)

        # The maximum product is obtained by the first two elements after subtracting 1 from each
        return (nums[0] - 1) * (nums[1] - 1)
