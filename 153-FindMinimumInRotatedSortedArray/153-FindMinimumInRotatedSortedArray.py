# Last updated: 10/07/2026, 11:59:55
class Solution(object):
    def findMin(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        end=len(nums)-1
        beg=0
        while beg<end:
            mid=(beg+end)//2
            if nums[mid]>nums[end]:
                beg=mid+1
            elif nums[mid]<nums[end]:
                end=mid
        return(nums[beg])            



       