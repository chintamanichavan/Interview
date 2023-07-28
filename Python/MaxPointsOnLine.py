from collections import defaultdict
from math import gcd

class Solution():
    def maxPoints(self, points):
        def calculate_slope(p1, p2):  # Renamed to 'calculate_slope'
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return (dy, dx) if dx == 0 else (dy / gcd(dy, dx), dx / gcd(dy, dx))

        n = len(points)
        if n < 3:
            return n

        max_points = 0
        for i in range(n):
            lines = defaultdict(int)
            duplicates = 1
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    duplicates += 1
                else:
                    lines[calculate_slope(points[i], points[j])] += 1  # Use 'calculate_slope' here
            max_points = max(max_points, duplicates)
            for slope in lines:
                max_points = max(max_points, lines[slope] + duplicates)
        return max_points


def main():
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    s = Solution()
    res = s.maxPoints(points)
    print(res)

if __name__ == '__main__':
    main()
