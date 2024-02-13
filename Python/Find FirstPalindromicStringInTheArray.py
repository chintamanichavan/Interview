class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        """
        Returns the first palindromic string in the array.

        Args:
            words: A list of strings.

        Returns:
            The first palindromic string in the array, or an empty string if no such string exists.
        """

        for word in words:
            if word == word[::-1]:  # Check if the word is a palindrome
                return word
        return ""  # No palindrome found
