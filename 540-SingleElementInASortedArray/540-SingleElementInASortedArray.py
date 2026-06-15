# Last updated: 14/06/2026, 23:03:17
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg=0
        end=len(nums)-1
        while beg<end:
            mid=(beg+end)//2
            
            if mid%2 == 1:
                mid=mid-1
            if nums[mid] == nums[mid+1]:
                beg=mid+2
            else:
                end=mid
        return(nums[beg])             

       