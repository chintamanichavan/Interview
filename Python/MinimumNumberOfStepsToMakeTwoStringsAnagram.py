class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # Array to store character count; index 0 for 'a', 1 for 'b', and so on
        count_s = [0] * 26
        count_t = [0] * 26

        # Count frequency of each character in s and t
        for char in s:
            count_s[ord(char) - ord('a')] += 1
        for char in t:
            count_t[ord(char) - ord('a')] += 1

        # Calculate the number of steps to make t an anagram of s
        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])

        # Divide by 2 since each mismatched character in s and t contributes twice to the total
        return steps // 2
