
class Solution():
    def findMinArrowShots(self, points):

        points.sort(key=lambda x: x[1])

        arrows = 0
        curr_end = -float('inf')

        for start, end in points:
            if curr_end < start:
                curr_end = end
                arrows += 1

        return arrows


def main():
    points = [[10,16],[2,8],[1,6],[7,12]]
    s = Solution()

    result = s.findMinArrowShots(points)
    print(result)

if __name__ == '__main__':
    main()
