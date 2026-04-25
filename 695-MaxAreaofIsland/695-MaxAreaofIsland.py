# Last updated: 25/04/2026, 14:28:26
1class Solution(object):
2    def maxAreaOfIsland(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        max_area=0
8        u=len(grid)
9        v=len(grid[0])
10
11        def dfs(i,j):
12            if i>=u or j>=v or i<0 or j<0 or grid[i][j]==0:
13                return 0
14            else:
15                grid[i][j]=0
16                return(1+dfs(i,j-1)+dfs(i,j+1)+dfs(i+1,j)+dfs(i-1,j))    
17
18        for i in range(u):
19            for j in range(v):
20                if grid[i][j]==1:
21                    max_area=max(max_area,dfs(i,j))   
22
23        return(max_area)            
24
25