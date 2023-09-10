def countOrders(n):
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * (2 * i - 1) * i) % mod
    
    return dp[n]

# Example usage:
print(countOrders(1))  # Output: 1
print(countOrders(2))  # Output: 6
print(countOrders(3))  # Output: 90
