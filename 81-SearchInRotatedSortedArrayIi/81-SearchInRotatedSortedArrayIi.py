# Last updated: 10/12/2025, 07:42:45
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        beg=0
        end=len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target:
                return (True)
            if nums[beg] == nums[mid] == nums[end]:
                beg+=1
                end-=1   
                continue
            if nums[beg]<=nums[mid]: #left is sorted
                if nums[beg]<=target<nums[mid]:
                    end=mid-1
                else:
                    beg=mid+1
            else: #right is sorted
                if nums[mid]<target<=nums[end]:
                    beg=mid+1
                else:
                    end=mid-1  
        return(False)                          
