# Last updated: 14/06/2026, 23:01:29
class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return (n)
        else:
            return(n*2)    
        