# Last updated: 31/10/2026, 19:06:08
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(1,n//2+1):
            l.append(i)
            l.append(-i)
        if n % 2 == 1: 
            l.append(0) 
        return(l)    


            
        