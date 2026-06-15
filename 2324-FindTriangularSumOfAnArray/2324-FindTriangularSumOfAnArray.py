# Last updated: 14/06/2026, 23:01:32
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums)>1:
            l=[]
            for i in range(len(nums)-1):
                l.append((nums[i]+nums[i+1])%10)
            nums=l
        return(nums[0])        


        