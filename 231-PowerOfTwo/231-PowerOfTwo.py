# Last updated: 10/12/2025, 07:42:06
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range (0,32):
            if 2**i==n:
                return (True)
        return (False)
        