#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names, heights):
        # Combine names and heights into a list of tuples
        people = list(zip(names, heights))
        
        # Sort the list of tuples by height in descending order
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the names from the sorted list of tuples
        sorted_names = [person[0] for person in people]
        
        return sorted_names
        
# @lc code=end

