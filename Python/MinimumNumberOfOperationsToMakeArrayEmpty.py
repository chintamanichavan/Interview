class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)  # Count the frequency of each element
        operations = 0

        for count in freq.values():
            if count == 1:
                # If any element occurs only once, it's impossible to make the array empty
                return -1

            # Apply operations based on the frequency
            operations += count // 3 + (1 if count % 3 else 0)

        return operations
