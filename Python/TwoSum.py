from typing import List
class TwoSum(object):

    def __init__(self, nums: List[int], target: int):
        self.nums= nums
        self.target = target

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for num in nums:
            numsDict[num] = num
        
        for num in nums:

            if ((target - num) in numsDict):
                print("The pair is {} {}".format(num, target - num))
                return [num, target - num]

        return None


nums = [2,7,11,15]
target = 9
object = TwoSum(nums, target)
object.twoSum(nums,target)
