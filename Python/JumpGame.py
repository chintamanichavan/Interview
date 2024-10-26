
class Solution():
    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0

    # print(canJump([2, 3, 1, 1, 4]))  # Returns: True
    # print(canJump([3, 2, 1, 0, 4]))  # Returns: False

    # Returns: True
        print(canJump([3,2,1,0,4]))  # Returns: False

if __name__ == '__main__':
    s = Solution()
    res = s.canJump([2,3,1,1,4])
    print(res)
