# Last updated: 25/07/2026, 13:28:47
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict1=[]
        max_prod=0
        for char in str(n):
            dict1.append(int(char))
        dict1.sort(reverse=True)    
        return(dict1[0]*dict1[1])