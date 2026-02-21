# Last updated: 20/02/2026, 20:50:11
1class Solution(object):
2    def countPrimeSetBits(self, left, right):
3        """
4        :type left: int
5        :type right: int
6        :rtype: int
7        """
8        p=0
9        primes = {2,3,5,7,11,13,17,19}
10        for i in range(left,right+1):
11            m=bin(i)[2:]
12            bits=0
13            for char in str(m):
14                if int(char) == 1:
15                    bits+=1
16            if bits in primes:
17                p+=1   
18        return(p)             
19        