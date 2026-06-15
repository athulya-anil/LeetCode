# Last updated: 14/06/2026, 23:03:29
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range (0,32):
            if 4**i==n:
                return (True)
        return (False)

