# Last updated: 04/07/2026, 00:21:25
1class Solution(object):
2    def numIslands(self, grid):
3        """
4        :type grid: List[List[str]]
5        :rtype: int
6        """
7        u=len(grid)
8        v=len(grid[0])
9        island=0
10
11        def dfs(i,j):
12            if i>=u or j>=v or i<0 or j<0 or grid[i][j]=="0":
13                return 0
14            else:    
15                grid[i][j]="0"
16                dfs(i,j+1)
17                dfs(i-1,j)
18                dfs(i,j-1)
19                dfs(i+1,j)
20
21        for i in range(u):
22            for j in range(v):
23                if grid[i][j]=="1":
24                    island+=1
25                    dfs(i,j)
26
27        return (island)            