from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:

        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

def main():
    nums = [0,1,0,1,0,1,99]
    s = Solution()
    res = s.singleNumber(nums)
    print(res)

if __name__ == '__main__':
    main()
