class Solution:
    def minSubArrayLen(target, nums):
        n = len(nums)
        left = 0
        sum = 0
        minLen = inf

        for right in range(n):
            sum += nums[right]

            while sum >= target:
                minLen = min(minLen, right - left + 1)
                sum -= nums[left]
                left += 1

        if minLen == inf:
            return 0
        return minLen

def main():
    target = 7
    nums = [2,3,1,2,4,3]
    s = Solution()
    s.minimumSubArrayLen(target, nums)

if __name__ == '__main__':
    main()
