#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            n = len(formula)
            i = 0
            
            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiple = int(formula[i_start:i] or 1)
                    for atom, count in top.items():
                        stack[-1][atom] += count * multiple
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    atom = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[i_start:i] or 1)
                    stack[-1][atom] += count
        
        stack = [defaultdict(int)]
        parse()
        
        result = ''
        for atom in sorted(stack[0]):
            count = stack[0][atom]
            result += atom + (str(count) if count > 1 else '')
        
        return result

# @lc code=end

