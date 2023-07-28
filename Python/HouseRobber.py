
class Solution():
    def rob(self, nums):
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

def main():
    nums = [1,2,3,1]
    s = Solution()
    res = s.rob(nums)
    print(res)

if __name__ == '__main__':
    main()
