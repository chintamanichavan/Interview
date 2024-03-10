class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums1:
          d[n] = 1

        for n in nums2:
		  # Check if n is in dictionary and not in the result
          if n in d and d[n]:
            res.append(n)
            d[n] -= 1 # It will set the value of d[n] = 0 which will indicate we already added n in result
        return res
