class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        """
        Finds the majority element in a list of numbers.

        Args:
            nums: A list of numbers.

        Returns:
            The majority element in the list.
        """

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
