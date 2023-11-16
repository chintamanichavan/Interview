class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Convert each binary string to an integer and add to a set for fast lookup
        seen = {int(num, 2) for num in nums}
        n = len(nums[0])

        # Generate all possible binary strings of length n
        for i in range(2**n):
            if i not in seen:
                # Format the number back into a binary string of length n
                return format(i, '0' + str(n) + 'b')
