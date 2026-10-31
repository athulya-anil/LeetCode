# Last updated: 31/10/2026, 19:01:32
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