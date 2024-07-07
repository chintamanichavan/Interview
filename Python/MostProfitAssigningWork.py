
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Step 1: Pair jobs with their profits and sort by difficulty
        jobs = sorted(zip(difficulty, profit))

        # Step 2: Sort the worker array
        worker.sort()

        # Step 3: Initialize variables
        max_profit = 0
        best_profit = 0
        job_index = 0
        n = len(jobs)

        # Step 4: Iterate through each worker and calculate the maximum profit
        for ability in worker:
            while job_index < n and jobs[job_index][0] <= ability:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            max_profit += best_profit

        return max_profit

# Example usage:
sol = Solution()
print(sol.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))  # Output: 100
print(sol.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))  # Output: 0
