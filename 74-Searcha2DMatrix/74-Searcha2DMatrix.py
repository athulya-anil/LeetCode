# Last updated: 30/12/2025, 22:12:45
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        r=len(matrix)
9        c=len(matrix[0])
10        beg=0
11        end=(r*c)-1
12        while beg<=end:
13            mid=(beg+end)//2
14            i=mid//c
15            j=mid %c
16
17            if matrix[i][j]==target:
18                return True
19            elif matrix[i][j] < target:  
20                beg=mid+1
21            else:
22                end=mid-1    
23        return False 
24  