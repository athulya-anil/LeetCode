# Last updated: 04/07/2026, 01:20:37
1class Solution(object):
2    def closedIsland(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        u=len(grid)
8        v=len(grid[0])
9        island=0
10
11        def dfs(i,j):
12            if i<0 or j<0 or i>= u or j>=v:
13                return False
14            if grid[i][j] == 1:
15                return True    
16
17            grid[i][j]=1
18
19            right = dfs(i, j + 1)
20            left = dfs(i, j - 1)
21            up = dfs(i - 1, j)
22            down = dfs(i + 1, j)    
23
24            return(up and down and right and left)
25        
26        for i in range(u):
27            for j in range(v):
28                if grid[i][j] == 0:
29                    if dfs(i,j):
30                        island+=1
31                    
32        return(island)            
33