# Last updated: 10/12/2025, 07:39:33
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
                
        
        