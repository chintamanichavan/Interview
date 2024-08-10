class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:


        def distance(point1, point2):
            return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))

        total_time = 0
        for i in range(len(points) - 1):
            total_time += distance(points[i], points[i + 1])

        return total_time
