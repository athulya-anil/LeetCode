# Last updated: 14/06/2026, 23:02:40
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        ans = []
        current = 0

        for bit in nums:
            current = (current * 2 + bit) % 5
            ans.append(current == 0)

        return ans
