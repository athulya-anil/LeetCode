# Last updated: 14/06/2026, 23:03:45
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n !=1:
            if n in seen:
                return False
            seen.add(n)

            new_n = 0
            for digit in str(n):
                new_n += int(digit)**2
            n = new_n
        return (True)  
        
        