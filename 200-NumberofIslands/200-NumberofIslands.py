# Last updated: 15/04/2026, 06:13:04
1class Solution(object):
2    def numIslands(self, grid):
3        """
4        :type grid: List[List[str]]
5        :rtype: int
6        """
7        island=0
8        u=len(grid)
9        v=len(grid[0])
10        def dfs(i,j):
11            if i<0 or j<0 or i>=u or j>=v or grid[i][j]!="1":
12                return 0
13            else:
14                grid[i][j]="0"
15                dfs(i,j-1)
16                dfs(i,j+1)
17                dfs(i-1,j)
18                dfs(i+1,j)    
19
20        for i in range (u):
21            for j in range(v):
22                if grid[i][j]== "1":
23                    island+=1
24                    dfs(i,j)
25
26        return (island)
27        