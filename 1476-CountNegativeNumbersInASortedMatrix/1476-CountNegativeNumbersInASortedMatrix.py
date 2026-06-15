# Last updated: 14/06/2026, 23:02:12

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid[0])
        count=0
        for row in grid:
            l=0
            r=n-1
            first_negative=n

            while l<=r:
                mid=(l+r)//2
                if row[mid]<0:
                    first_negative=mid
                    r=mid-1
                else:
                    l=mid+1    
            count+=(n-first_negative)
        return(count)            