class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and log(num,4).is_integer()

# review 2024-08-15
