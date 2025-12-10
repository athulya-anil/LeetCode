# Last updated: 10/12/2025, 07:41:19
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)

        while i < n - 1:   
            if bits[i] == 1:
                i += 2   
            else:
                i += 1  

        return i == n - 1
        
        