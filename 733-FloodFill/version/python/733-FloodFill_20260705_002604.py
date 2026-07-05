# Last updated: 05/07/2026, 00:26:04
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
11        def dfs(i,j):
12            if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j] != oldColor or image[i][j] == color:
13                return
14
15            image[i][j]=color
16            dfs(i+1,j)
17            dfs(i-1,j)
18            dfs(i,j+1)
19            dfs(i,j-1)
20  
21        dfs(sr,sc)    
22        return(image)
23        
24
25     