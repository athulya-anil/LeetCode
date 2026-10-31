# Last updated: 31/10/2026, 19:02:33
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


        