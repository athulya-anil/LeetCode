# Last updated: 02/01/2026, 22:27:35
1class Solution(object):
2    def repeatedNTimes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        seen = set()
8        for i in nums:
9            if i not in seen:
10                seen.add(i)
11            else:
12                return i    