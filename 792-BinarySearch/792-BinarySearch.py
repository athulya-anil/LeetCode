# Last updated: 14/06/2026, 23:02:54
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg=0
        end=len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target:
                return(mid)
            elif nums[mid]<target:
                beg=mid+1
            else:
                end=mid-1
        return(-1)                
       