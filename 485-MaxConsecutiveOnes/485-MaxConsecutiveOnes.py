# Last updated: 10/12/2025, 07:41:43
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_counter = 0
        counter = 0
        for i in range (0,len(nums)):
            if nums[i]==1:
                counter +=1
                max_counter = max(max_counter,counter)
            else:
                counter = 0    
        return (max_counter)        
        