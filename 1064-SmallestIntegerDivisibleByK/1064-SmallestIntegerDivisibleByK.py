# Last updated: 10/12/2025, 07:41:06
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
        