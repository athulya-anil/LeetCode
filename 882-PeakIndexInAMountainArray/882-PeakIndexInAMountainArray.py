# Last updated: 10/12/2025, 07:41:14
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        beg=0
        end=len(arr)-1
        while beg<end:
            mid=(beg+end)//2
            if arr[mid]<=arr[mid+1]:
                beg=mid+1
            else:
                end=mid
        return(beg)            
        