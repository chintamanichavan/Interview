def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # There's one way to make a sum of 0.
    
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    
    return dp[target]

# Example usage:
nums1 = [1, 2, 3]
target1 = 4
print(combinationSum4(nums1, target1))  # Output: 7

nums2 = [9]
target2 = 3
print(combinationSum4(nums2, target2))  # Output: 0
