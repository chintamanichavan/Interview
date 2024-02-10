class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expandAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        palindromic_count = 0
        for i in range(len(s)):
            # Count odd-length palindromes
            palindromic_count += expandAroundCenter(i, i)
            # Count even-length palindromes
            palindromic_count += expandAroundCenter(i, i + 1)

        return palindromic_count
