# Last updated: 05/01/2026, 23:06:29
1
2class Solution(object):
3    def countNegatives(self, grid):
4        """
5        :type grid: List[List[int]]
6        :rtype: int
7        """
8        n=len(grid[0])
9        count=0
10        for row in grid:
11            l=0
12            r=n-1
13            first_negative=n
14
15            while l<=r:
16                mid=(l+r)//2
17                if row[mid]<0:
18                    first_negative=mid
19                    r=mid-1
20                else:
21                    l=mid+1    
22            count+=(n-first_negative)
23        return(count)            