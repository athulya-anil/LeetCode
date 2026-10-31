# Last updated: 31/10/2026, 19:01:07
class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        place=1
        l=[]

        while n>0:
            digit = n%10
            if digit != 0:
                l.append(digit*place)
            place*=10
            n=n//10
        return(l[::-1])        
                
        
        