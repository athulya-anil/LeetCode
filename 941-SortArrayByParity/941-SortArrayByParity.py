# Last updated: 10/12/2025, 07:41:11
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            # If left is odd and right is even -> swap them
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            
            # Move left pointer if it's already even
            if nums[left] % 2 == 0:
                left += 1
            
            # Move right pointer if it's already odd
            if nums[right] % 2 == 1:
                right -= 1
                
        return nums
        