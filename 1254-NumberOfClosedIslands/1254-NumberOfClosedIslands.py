# Last updated: 31/10/2026, 19:06:21
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        u=len(grid)
        v=len(grid[0])
        island=0

        def dfs(i,j):
            if i<0 or j<0 or i>=u or j>=v:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1

            left=dfs(i,j-1)
            right=dfs(i,j+1)
            up=dfs(i+1,j)
            down=dfs(i-1,j)      

            return(left and right and up and down)  

        for i in range(u):
            for j in range(v):
                if grid[i][j]==0 and dfs(i,j):
                    island+=1
        return (island)            
        