# Last updated: 14/06/2026, 23:02:46
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