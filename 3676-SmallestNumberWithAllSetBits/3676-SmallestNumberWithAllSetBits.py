# Last updated: 14/06/2026, 23:01:15
class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        while (1 << k) - 1 < n:
            k += 1
        return (1 << k) - 1