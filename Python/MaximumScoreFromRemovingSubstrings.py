#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#

# @lc code=start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        letter_a = "a"
        if x < y:
            # change the role of 'a' and 'b'
            letter_a = "b"
            x, y = y, x

        total = 0
        dxy = x-y
        ab_count = a_count = b_count = 0

        for char in s:
            if char not in "ab":
                if b_count > a_count:
                    a_count, b_count = b_count, a_count
                if a_count > 0:
                    total += ab_count*dxy+b_count*y
                    ab_count = a_count = b_count = 0

            elif char == letter_a:
                a_count += 1

            else:
                # last letter is b.
                # form ab if there is free a 
                # or change ba to b + ab
                b_count += 1
                if a_count > ab_count:
                    ab_count += 1
                
        total += ab_count*dxy+min(a_count, b_count)*y
              
        return total        
# @lc code=end

