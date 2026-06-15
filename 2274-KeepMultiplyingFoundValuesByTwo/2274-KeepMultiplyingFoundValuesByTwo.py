# Last updated: 14/06/2026, 23:01:34
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


        