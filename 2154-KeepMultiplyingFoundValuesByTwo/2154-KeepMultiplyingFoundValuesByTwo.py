# Last updated: 31/10/2026, 19:02:51
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


        