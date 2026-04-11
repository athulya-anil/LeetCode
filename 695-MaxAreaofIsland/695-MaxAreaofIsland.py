# Last updated: 11/04/2026, 18:11:20
1class Solution(object):
2    def maxAreaOfIsland(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        m=len(grid)
8        n=len(grid[0])
9
10        def dfs(i,j):
11            if i<0 or j<0 or i>=m or j>=n or grid[i][j] != 1:
12                return 0
13            else:
14                grid[i][j]=0    
15                return 1+ dfs(i,j-1) + dfs(i,j+1) + dfs(i+1,j) + dfs(i-1,j)
16
17        max_area=0
18        for i in range(m):
19            for j in range(n):
20                if grid[i][j]==1:
21                    max_area=max(max_area,dfs(i,j))
22
23        return max_area
24
25        