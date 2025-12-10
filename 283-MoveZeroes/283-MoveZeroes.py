# Last updated: 10/12/2025, 07:41:55
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow=0
        fast=0

        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
            fast+=1    
        