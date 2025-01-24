class Solution:
    def numDecodings(self, s: str) -> int:

        # Edge case: If the string starts with '0', it can't be decoded
        if not s or s[0] == '0':
            return 0

        # Initialize the two previous values for dynamic programming
        prev, curr = 1, 1

        for i in range(1, len(s)):
            temp = 0
            # Single digit decoding is valid if the current digit is not '0'
            if s[i] != '0':
                temp += curr
            # Two digit decoding is valid if the number formed by last two digits is between 10 and 26
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += prev

            prev, curr = curr, temp

        return curr
