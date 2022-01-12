# def maxArea(self, height: List[int]) -> int:
    
#     # length of input array
#     size = len(height)
    
#     # two pointers, left init as 0, right init as size-1
#     left, right = 0, size-1
    
#     # maximal width between leftmost stick and rightmost stick
#     max_width = size - 1
    
#     # area also known as the amount of water
#     area = 0
    
#     # trade-off between width and height
#     # scan each possible width and compute maximal area
#     for width in range(max_width, 0, -1):
        
#         if height[left] < height[right]:
#             # the height of lefthand side is shorter
#             area = max(area, width * height[left] )
            
#             # update left index to righthand side
#             left += 1
            
#         else:
#             # the height of righthand side is shorter
#             area = max(area, width * height[right] )
            
#             # update right index to lefthand side
#             right -= 1
            
#     return area

from typing import List


def maxArea(height: List[int]) -> int:
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

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)