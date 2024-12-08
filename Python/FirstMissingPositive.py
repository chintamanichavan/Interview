from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        return 0


def main():
    s = Solution()
    nums = [2,1,0]
    s.firstMissingPositive(nums)

if __name__ == '__main__':
    main()
