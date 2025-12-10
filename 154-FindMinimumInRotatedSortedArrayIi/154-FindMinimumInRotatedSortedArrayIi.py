# Last updated: 10/12/2025, 07:42:33
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg=0
        end=len(nums)-1
        while beg<end:
            mid=(beg+end)//2
            if nums[mid] > nums[end]:
                beg=mid+1
            elif nums[mid] < nums[end]:
                end=mid
            else:
                end-=1    
        return(nums[beg])            



        