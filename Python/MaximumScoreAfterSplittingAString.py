class Solution:
    def maxScore(self, s: str) -> int:
        
        """
        Optimized function to calculate the maximum score after splitting the string into two non-empty substrings.
        """
        # Count the initial number of ones in the entire string.
        total_ones = s.count('1')

        # Initialize the score with the count of ones (as if the entire string is the right substring).
        score = total_ones
        max_score = 0

        # Iterate through the string, adjusting the score and keeping track of the maximum.
        for i in range(len(s) - 1):  # Exclude the last character to avoid empty right substring
            if s[i] == '0':
                score += 1  # Increment score for '0' as it contributes to the left substring
            else:
                score -= 1  # Decrement score for '1' as it moves from right to left substring

            max_score = max(max_score, score)

        return max_score
