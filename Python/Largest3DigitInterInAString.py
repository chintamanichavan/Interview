class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        max_good_int = ""
        for i in range(len(num) - 2):
            # Extract a substring of length 3
            substring = num[i:i+3]
            # Check if all characters in the substring are the same
            if substring[0] == substring[1] == substring[2]:
                # Update max_good_int if the current substring is greater
                if substring > max_good_int:
                    max_good_int = substring
        return max_good_int
