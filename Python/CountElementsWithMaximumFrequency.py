class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = {}

        # Calculate frequency of each element
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Find the maximum frequency
        max_frequency = max(frequency.values())

        # Count elements with maximum frequency
        count_max_freq = sum(f == max_frequency for f in frequency.values())

        # Return the total count of elements with the maximum frequency
        return count_max_freq * max_frequency

