# Last updated: 27/12/2025, 19:41:53
1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        if n <= 2:
8            return n
9
10        prev1, prev2 = 2, 1  # dp[2], dp[1]
11
12        for _ in range(3, n + 1):
13            curr = prev1 + prev2
14            prev2 = prev1
15            prev1 = curr
16
17        return prev1
18
19        