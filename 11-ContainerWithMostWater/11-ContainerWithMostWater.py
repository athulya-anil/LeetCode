# Last updated: 10/07/2026, 12:01:05
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        area=0
        while left<right:
            h=min(height[left],height[right])
            area=max(area,h*(right-left))
            if height[left]<height[right]:
                left+=1
            else:    
                right-=1
        return area    

    