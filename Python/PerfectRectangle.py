from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # An exact cover (no gaps, no overlaps) holds iff: (1) the summed area of the pieces equals
        # the area of their bounding box, and (2) every internal corner cancels out — only the four
        # bounding-box corners appear an odd number of times. Corners toggle in a set.
        area = 0
        minx = miny = float("inf")
        maxx = maxy = float("-inf")
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            minx, miny = min(minx, x1), min(miny, y1)
            maxx, maxy = max(maxx, x2), max(maxy, y2)
            for pt in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if pt in corners:
                    corners.remove(pt)
                else:
                    corners.add(pt)

        expected = {(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)}
        if corners != expected:
            return False
        return area == (maxx - minx) * (maxy - miny)


if __name__ == "__main__":
    s = Solution()
    print(
        s.isRectangleCover(
            [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
        )
    )  # True
    print(
        s.isRectangleCover([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]])
    )  # False (gap)
    print(
        s.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]])
    )  # False (overlap)
    print(s.isRectangleCover([[0, 0, 1, 1]]))  # True
