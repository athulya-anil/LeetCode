# Last updated: 04/11/2026, 20:45:46
1class Solution(object):
2    def maxArea(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        max_area=0
8        left=0
9        right=len(height)-1
10        while left<right:
11            h=min(height[left],height[right])
12            area=h*(right-left)
13            max_area=max(area,max_area)
14
15            if height[left]<height[right]:
16                left+=1
17            else:
18                right-=1
19        return(max_area)            
20        