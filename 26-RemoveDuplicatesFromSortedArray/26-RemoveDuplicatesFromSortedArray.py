# Last updated: 10/07/2026, 12:01:00
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        return(slow+1)        

        