# Last updated: 31/10/2026, 19:08:21
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        beg=0
        end=len(arr)-1
        while beg<end:
            mid=(beg+end)//2

            if arr[mid]<arr[mid+1]:
                beg=mid+1
            else:
                end=mid   
                 
        return (beg)        
        