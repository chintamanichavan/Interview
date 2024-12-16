class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """ Count the number of nice pairs in the array """
        MOD = 10**9 + 7

        def rev(x):
            """ Reverse a non-negative integer x """
            return int(str(x)[::-1])

        # Create a dictionary to count the occurrences of nums[i] - rev(nums[i])
        freq = {}
        for num in nums:
            diff = num - rev(num)
            freq[diff] = freq.get(diff, 0) + 1

        # Calculate the number of nice pairs
        nice_pairs_count = 0
        for count in freq.values():
            nice_pairs_count += (count * (count - 1) // 2) % MOD

        return nice_pairs_count % MOD
