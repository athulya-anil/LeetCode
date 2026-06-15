# Last updated: 14/06/2026, 23:02:43
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