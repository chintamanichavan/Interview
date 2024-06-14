
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # nums.sort()
        # start,count = nums[0], 0
        # for i in range(1, len(nums)):
        #     if nums[i] <= start:
        #         count += start-nums[i]+1
        #     start = max(nums[i], start+1)
        # return count

        dp = [0]*(max(nums)+ 1)
        for num in nums:
            dp[num] += 1

        count = 0
        for i in range(len(dp)-1):
            if dp[i] > 1:
                count += dp[i]-1
                dp[i+1] += (dp[i]-1)
        count += dp[-1]*(dp[-1]-1)//2
        return count


