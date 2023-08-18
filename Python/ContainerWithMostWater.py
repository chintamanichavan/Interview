class Solution:
    def maxArea(self, height):
        maxArea = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                area = min(height[i], height[j]) * width
                maxArea = max(maxArea, area)

        return maxArea


def main():
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    s.maxArea(height)
    result = s.maxArea(height)
    print(result)

if __name__ == '__main__':
    main()
