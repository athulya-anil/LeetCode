# Last updated: 10/12/2025, 07:42:04
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        col=len(matrix[0])

        r=0
        c=col-1

        while r<row and c>=0:
            if matrix[r][c]==target:
                return(True)
            elif matrix[r][c]<target:
                r=r+1
            else:
                c=c-1      
        return(False)          
        