# Last updated: 31/10/2026, 19:07:57
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i]=nums[i]**2
            i=+1
        nums.sort()
        return(nums)