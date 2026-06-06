from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Single pass: left accumulates the prefix; right = total - left - nums[i].
        total = sum(nums)
        left = 0
        ans = []
        for x in nums:
            right = total - left - x
            ans.append(abs(left - right))
            left += x
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.leftRightDifference([10, 4, 8, 3]))  # [15, 1, 11, 22]
    print(s.leftRightDifference([1]))            # [0]
