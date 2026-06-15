# Last updated: 14/06/2026, 23:03:18
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
        