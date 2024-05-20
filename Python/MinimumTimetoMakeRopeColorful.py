class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        maxTimeInGroup = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # If current balloon is the same color as the previous one, 
                # add the smaller time (between current and maxTimeInGroup) to totalTime
                totalTime += min(maxTimeInGroup, neededTime[i])
                # Update maxTimeInGroup to the maximum time in the current group
                maxTimeInGroup = max(maxTimeInGroup, neededTime[i])
            else:
                # Reset maxTimeInGroup for the next group of same-colored balloons
                maxTimeInGroup = neededTime[i]

        return totalTime
