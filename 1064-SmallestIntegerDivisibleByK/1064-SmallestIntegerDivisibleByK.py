# Last updated: 14/06/2026, 23:02:41
class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0
        for length in range(1, k+1):      # pigeonhole principle
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        
        return -1
        