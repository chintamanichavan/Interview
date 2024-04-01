class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim leading and trailing spaces and split the string into words
        r = s.strip().split()
        # Return the length of the last word
        return len(r[-1])
