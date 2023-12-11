class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4
        for i in range(len(arr)):
            if arr.count(arr[i]) > threshold:
                return arr[i]
