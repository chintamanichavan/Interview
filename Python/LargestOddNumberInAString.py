class Solution:
    def largestOddNumber(self, num: str) -> str:

        """
        Function to find the largest-valued odd integer that is a non-empty substring of num,
        or an empty string if no odd integer exists.
        """
        # Iterate backwards through the string
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  # Check if the digit is odd
                return num[:i + 1]  # Return the substring ending with the odd digit
        return ""  # Return empty string if no odd integer exists
