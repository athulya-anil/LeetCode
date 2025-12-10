# Last updated: 10/12/2025, 07:41:08
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