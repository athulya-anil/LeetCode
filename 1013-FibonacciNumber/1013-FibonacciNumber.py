# Last updated: 10/12/2025, 07:41:09
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n == 0:
            return 0
        while n == 1:
            return 1
        return (self.fib(n-1)+self.fib(n-2))
        