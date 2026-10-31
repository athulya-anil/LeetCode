# Last updated: 31/10/2026, 19:01:11
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        f1=0
        f2=1
        f3=1

        while f1+f2+f3<=n:
            if f1+f2+f3==n:
                return True
                
            f1,f2,f3=f2,f3,f2+f3    
        return False    
        
        
        
        