import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = []
        
        for num in nums:
            # Find the index where 'num' should be inserted to maintain the increasing order
            idx = bisect.bisect_left(dp, num)
            
            # If 'num' is greater than any element in 'dp', append it
            if idx == len(dp):
                dp.append(num)
            else:
                # Replace the element at the found index with 'num'
                dp[idx] = num
        
        # The length of 'dp' is the length of the longest increasing subsequence
        return len(dp)
