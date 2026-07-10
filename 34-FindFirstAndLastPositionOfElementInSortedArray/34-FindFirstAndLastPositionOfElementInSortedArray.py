# Last updated: 10/07/2026, 12:00:56
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_pos():
            beg=0
            end=len(nums)-1
            ans=-1
            while beg<=end:
                mid=(beg+end)//2
                if nums[mid]==target:
                    ans=mid
                    end=mid-1
                elif nums[mid]<target:
                    beg=mid+1
                else:
                    end=mid-1
            return(ans)      
        def last_pos():
            beg=0
            end=len(nums)-1
            ans=-1
            while beg<=end:
                mid=(beg+end)//2
                if nums[mid]==target:
                    ans=mid
                    beg=mid+1
                elif nums[mid]<target:
                    beg=mid+1
                else:
                    end=mid-1
            return(ans)
        return(first_pos(),last_pos())          
        