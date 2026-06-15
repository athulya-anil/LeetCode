# Last updated: 14/06/2026, 23:03:36
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num>9:
            sum=0
            for digit in str(num):
                sum += int(digit)
            num=sum    
        return(num)        