# Last updated: 14/06/2026, 23:01:57
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        beg=1
        while n>0:
            for i in range (beg,beg+ min(n,7)):
                total+=i
            beg+=1   
            n-=7    
        return(total)     

    

        