class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minP, maxP = -1, -1
        start = 0
        for end, n in enumerate(nums):
            if n < minK or n>maxK:
                minP, maxP = -1,-1
                start = end+1
            else:
                # print(min_,max_)
                if n == minK:
                    minP = end
                if n == maxK:
                    maxP = end
                if minP == -1 or maxP == -1:
                    continue
                if minP > maxP:
                    ans += maxP-start+1
                else:
                    ans += minP-start+1

        return ans
