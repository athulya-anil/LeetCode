# Last updated: 10/12/2025, 07:42:09
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


        
        