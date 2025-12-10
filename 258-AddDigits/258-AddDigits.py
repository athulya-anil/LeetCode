# Last updated: 10/12/2025, 07:42:01
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