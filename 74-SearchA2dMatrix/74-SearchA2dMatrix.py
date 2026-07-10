# Last updated: 10/07/2026, 12:00:38
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r=len(matrix)
        c=len(matrix[0])
        beg=0
        end=(r*c)-1
        while beg<=end:
            mid=(beg+end)//2
            i=mid//c
            j=mid %c

            if matrix[i][j]==target:
                return True
            elif matrix[i][j] < target:  
                beg=mid+1
            else:
                end=mid-1    
        return False 
  