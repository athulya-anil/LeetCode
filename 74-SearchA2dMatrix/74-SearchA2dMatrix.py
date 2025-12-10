# Last updated: 10/12/2025, 07:42:46
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        c=len(matrix)
        r=len(matrix[0])
        beg=0
        end=c*r-1
        while beg<=end:
            mid=(beg+end)//2
            i=mid//r
            j=mid%r
            if matrix[i][j]==target:
                return(True)
            elif matrix[i][j]<target:
                beg=mid+1
            else:
                end=mid-1
        return(False)                
        
       