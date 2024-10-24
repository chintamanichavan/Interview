from typing import List
class Solution(object):

    def __init__(self, nums: List[int], target: int):
        self.nums = nums
        self.target = target

    def binary_search(self, nums: List[int], target: int) -> int:
        begin_index = 0
        end_index = len(nums) - 1
        while begin_index <= end_index:
            mid_index = (end_index + begin_index) // 2
            mid_index_value = nums[mid_index]
            if target == mid_index_value:
                return mid_index

            elif target < mid_index_value:
                end_index = mid_index - 1

            else:
                begin_index = mid_index + 1

        return -1


def main():
    s = Solution()
    nums = [-2, 3, 4, 7, 8, 9, 11, 13]
    target = 11
    s.binary_search(nums, target)

if __name__ == '__main__':
    main()
