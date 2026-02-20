class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        res = 1
        for i in range(1,len(arr)):
            if (arr[i] > res):
                res += 1
        return res
        

# review 2025-07-05

# review 2026-02-20
