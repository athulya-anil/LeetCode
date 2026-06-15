# Last updated: 14/06/2026, 23:03:43
from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # freq={}
        # freq=Counter(nums)
        # for count in freq.values():
        #     if count > 1:
        #         return (True)
        # return (False)    
        return (len(set(nums)) < len(nums))


        
        