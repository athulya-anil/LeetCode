# Last updated: 10/12/2025, 07:42:11
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        
        is_prime = [True] * n
        is_prime[0]=is_prime[1]=False   
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j]=False

        # for i in range (2,n):
        #     if is_prime[i]:
        #         print(i) 

        return sum(is_prime)      


        # def isprime(n):
        #     if n<=1:
        #         return False
        #     elif n == 2:
        #         return True    
        #     elif n%2==0:
        #         return False
        #     else:
        #         for i in range(3,int(n**0.5)+1,2):
        #             if n % i == 0:   
        #                 return False
        #         return True
        # return sum(isprime(i) for i in range(2,n))                



        