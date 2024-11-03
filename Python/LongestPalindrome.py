
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize an array to count occurrences of each character
        count = [0] * 128

        # Count the occurrences of each character in the string
        for char in s:
            count[ord(char)] += 1

        length = 0
        odd_found = False

        # Calculate the length of the longest palindrome
        for cnt in count:
            if cnt % 2 == 0:
                length += cnt
            else:
                length += cnt - 1
                odd_found = True

        # If there is at least one character with an odd count, add 1 to the length
        if odd_found:
            length += 1

        return length
