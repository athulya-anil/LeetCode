# Last updated: 14/06/2026, 23:02:59
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area=0
        u=len(grid)
        v=len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=u or j>=v or grid[i][j]==0:
                return 0
            else:
                grid[i][j]=0
                return(1+dfs(i,j-1)+dfs(i,j+1)+dfs(i-1,j)+dfs(i+1,j))    

        for i in range(u):
            for j in range(v):
                if grid[i][j]==1:
                    max_area=max(max_area,dfs(i,j))
        return (max_area)            