# Last updated: 31/10/2026, 19:08:04
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return i    