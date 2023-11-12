class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0
        count = 1

        for i in range(1, len(s)):
            # If the current character is the same as the previous, increment count
            if s[i] == s[i-1]:
                count += 1
            else:
                # Calculate the number of substrings for the previous character sequence
                total_count += count * (count + 1) // 2
                count = 1

        # Add the substrings count for the last character sequence
        total_count += count * (count + 1) // 2

        return total_count % MOD

