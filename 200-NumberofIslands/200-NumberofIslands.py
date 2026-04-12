# Last updated: 12/04/2026, 12:28:55
1class Solution(object):
2    def numIslands(self, grid):
3        """
4        :type grid: List[List[str]]
5        :rtype: int
6        """
7        island=0
8        u=len(grid)
9        v=len(grid[0])
10
11        def dfs(i,j):
12            if i<0 or j<0 or i>=u or j>=v or grid[i][j] !="1":
13                return 0
14            else:
15                grid[i][j]="0"
16                dfs(i-1,j) 
17                dfs(i+1,j)
18                dfs(i,j-1)
19                dfs(i,j+1)   
20
21        for i in range(u):
22            for j in range(v):
23                if grid[i][j]=="1":
24                    island+=1
25                    dfs(i,j)
26
27        return(island)        
28
29
30        
31            
32
33
34