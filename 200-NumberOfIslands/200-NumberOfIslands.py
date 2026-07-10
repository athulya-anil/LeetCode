# Last updated: 10/07/2026, 11:59:29
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        u=len(grid)
        v=len(grid[0])
        island=0

        def dfs(i,j):
            if i>=u or j>=v or i<0 or j<0 or grid[i][j]=="0":
                return 0
            else:    
                grid[i][j]="0"
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)

        for i in range(u):
            for j in range(v):
                if grid[i][j]=="1":
                    island+=1
                    dfs(i,j)

        return (island)            