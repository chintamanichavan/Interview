from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height) - 1
        while l < r:
            area = (r - 1) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        print(res)
        return res

def main():
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    s.maxArea(height)

if __name__ == '__main__':
    main()
