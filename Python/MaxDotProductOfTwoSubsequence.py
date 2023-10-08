def maxDotProduct(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[float('-inf')] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
            dp[i][j] = max(dp[i][j], nums1[i-1] * nums2[j-1])
            if i > 1 and j > 1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + nums1[i-1] * nums2[j-1])
                
    return dp[m][n]

# Test the function with the given examples
print(maxDotProduct([2,1,-2,5], [3,0,-6]))  # Expected output: 18
print(maxDotProduct([3,-2], [2,-6,7]))      # Expected output: 21
print(maxDotProduct([-1,-1], [1,1]))        # Expected output: -1
