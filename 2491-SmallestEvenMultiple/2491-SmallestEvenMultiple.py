# Last updated: 10/12/2025, 07:39:51
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            return(n)
        return(n*2)    