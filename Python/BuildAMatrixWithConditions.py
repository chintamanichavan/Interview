#
# @lc app=leetcode id=2392 lang=python3
#
# [2392] Build a Matrix With Conditions
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions, k):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            return topo_order if len(topo_order) == k else []
        
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix

# Example usage:
# k = 3
# rowConditions = [[1,2],[3,2]]
# colConditions = [[2,1],[3,2]]
# sol = Solution()
# print(sol.buildMatrix(k, rowConditions, colConditions))

        
# @lc code=end

