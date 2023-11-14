class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        # Set to store unique palindromes of length 3
        unique_palindromes = set()

        # Dictionary to store the first and last occurrence of each character
        char_indices = {}
        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = [i, i]
            else:
                char_indices[char][1] = i

        # Iterate through each character to find unique palindromes
        for char, (first, last) in char_indices.items():
            if first != last:
                # If a character occurs more than once, any character between its first and last occurrence
                # can form a palindrome with it
                unique_palindromes.update({char + mid_char + char for mid_char in set(s[first+1:last])})

        return len(unique_palindromes)
