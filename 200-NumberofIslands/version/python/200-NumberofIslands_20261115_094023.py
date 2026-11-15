# Last updated: 15/11/2026, 09:40:23
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        u=len(grid)
4        v=len(grid[0])
5        island=0
6        def dfs(i,j):
7            if i<0 or j<0 or i>=u or j>=v or grid[i][j] != "1":
8                return
9            else:
10                grid[i][j]="0"
11                dfs(i,j-1)
12                dfs(i,j+1)
13                dfs(i+1,j)
14                dfs(i-1,j)
15
16        for i in range(u):
17            for j in range(v):
18                if grid[i][j]=="1":
19                    island+=1 
20                    dfs(i,j)
21
22        return island            
23        