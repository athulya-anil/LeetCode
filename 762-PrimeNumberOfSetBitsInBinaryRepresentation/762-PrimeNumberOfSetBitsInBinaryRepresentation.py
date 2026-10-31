# Last updated: 31/10/2026, 19:08:41
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        p=0
        primes = {2,3,5,7,11,13,17,19}
        for i in range(left,right+1):
            m=bin(i)[2:]
            bits=0
            for char in str(m):
                if int(char) == 1:
                    bits+=1
            if bits in primes:
                p+=1   
        return(p)             
        