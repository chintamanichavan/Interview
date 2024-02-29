class Solution:
    def canMakeArithmeticProgression(self, arr):
        """Helper function to check if the array can be rearranged to form an arithmetic progression."""
        arr.sort()
        return all(arr[i] - arr[i - 1] == arr[1] - arr[0] for i in range(2, len(arr)))

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """Check if each subarray defined by l and r can form an arithmetic sequence."""
        answer = []
        for start, end in zip(l, r):
            subarray = nums[start:end + 1]
            answer.append(self.canMakeArithmeticProgression(subarray))
        return answer
