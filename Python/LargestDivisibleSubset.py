class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        nums.sort()
        n = len(nums)
        count = [1] * n
        prev = [-1] * n
        max_index = 0

        # Build up the count and prev arrays
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and count[j] + 1 > count[i]:
                    count[i] = count[j] + 1
                    prev[i] = j
                    if count[i] > count[max_index]:
                        max_index = i

        # Reconstruct the largest divisible subset
        largest_subset = []
        while max_index >= 0:
            largest_subset.append(nums[max_index])
            max_index = prev[max_index]

        return largest_subset[::-1]  # Reverse the subset to get it in ascending order
