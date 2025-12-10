# Last updated: 10/12/2025, 07:41:48
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(cap):
            sum=0
            sub_arr=1
            for i in nums:
                if i+sum>cap:
                    sum=0
                    sub_arr+=1
                sum+=i
            return sub_arr<=k         

        beg=max(nums)
        end=sum(nums)
        ans=end
        while beg<=end:
            mid=(beg+end)//2
            if canSplit(mid)==True:
                ans=mid
                end=mid-1
            else:
                beg=mid+1    
        return(ans)            
    