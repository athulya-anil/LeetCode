# Last updated: 12/04/2026, 12:34:45
1class Solution(object):
2    def maxAreaOfIsland(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        u=len(grid)
8        v=len(grid[0])
9        max_area=0
10
11        def dfs(i,j):
12            if i<0 or j<0 or i>=u or j>=v or grid[i][j] != 1:
13                return 0
14            else:
15                grid[i][j]=0
16                return(1+dfs(i+1,j)+dfs(i,j-1)+dfs(i-1,j)+dfs(i,j+1))    
17
18        for i in range(u):
19            for j in range(v):
20                if grid[i][j]==1:
21                    max_area=max(max_area,dfs(i,j))
22
23        return (max_area)            
24        