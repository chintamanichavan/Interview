#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        sub = list(s)
        i = len(sub) - 1
        while "(" in sub:
            if sub[i] == "(":
                for j in range(i, len(sub)):
                    if sub[j] == ")":
                        sub[i + 1 : j] = sub[i + 1 : j][::-1]
                        sub.pop(j)
                        sub.pop(i)
                        break
            i -= 1
        return "".join(sub)
        
# @lc code=end

