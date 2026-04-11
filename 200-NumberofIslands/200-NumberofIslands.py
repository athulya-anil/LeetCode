# Last updated: 11/04/2026, 15:05:41
1class Solution(object):
2    def numIslands(self, grid):
3        """
4        :type grid: List[List[str]]
5        :rtype: int
6        """
7        u=len(grid)
8        v=len(grid[0])
9
10        def dfs(i,j):
11            if (i<0 or i>=u or j<0 or j>=v or grid[i][j] != "1"):
12                return
13            else:
14                grid[i][j]="0"  
15                dfs(i,j+1) #right
16                dfs(i-1,j) #up
17                dfs(i+1,j) #down 
18                dfs(i,j-1) #left  
19        island=0
20        for i in range(u):
21            for j in range(v):    
22                if grid[i][j]=="1":
23                    island+=1
24                    dfs(i,j)
25
26        return(island)            
27            
28
29
30