# Last updated: 04/07/2026, 00:56:35
1class Solution(object):
2    def floodFill(self, image, sr, sc, color):
3        """
4        :type image: List[List[int]]
5        :type sr: int
6        :type sc: int
7        :type color: int
8        :rtype: List[List[int]]
9        """
10        oldColor=image[sr][sc]
11
12        def dfs(i,j):
13            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
14                return
15            
16            if image[i][j]==color or image[i][j]!=oldColor:
17                return 
18            else:     
19                image[i][j]=color
20                dfs(i,j-1)
21                dfs(i,j+1)
22                dfs(i-1,j)
23                dfs(i+1,j)
24
25        dfs(sr,sc)
26        return(image)    
27
28        