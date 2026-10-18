# Last updated: 18/10/2026, 14:00:09
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        u=len(grid)
4        v=len(grid[0])
5        island=0
6
7        def dfs(i,j):
8            if   i<0 or j<0 or i>=u or j>=v or grid[i][j] != "1":
9                return 
10            else:
11                grid[i][j]="0"
12                dfs(i,j-1)    
13                dfs(i,j+1) 
14                dfs(i-1,j) 
15                dfs(i+1,j) 
16
17        for i in range(u): 
18            for j in range(v):
19                if grid[i][j] == "1":
20                    island+=1
21                    dfs(i,j)
22        return island       
23
24       