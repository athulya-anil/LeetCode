# Last updated: 10/07/2026, 12:01:09
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        rev=[]
        n=x
        while n>0:
            rev.append(n%10)
            n=n//10
        orginal=rev[::-1]
        if orginal == rev:
            return True   
        else:
            return False
