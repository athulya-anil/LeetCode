# Last updated: 10/12/2025, 07:39:56
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        while original in nums:
            original*=2

        return original    


        