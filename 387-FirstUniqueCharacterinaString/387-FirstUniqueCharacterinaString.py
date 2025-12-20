# Last updated: 20/12/2025, 22:46:02
1class Solution(object):
2    def firstUniqChar(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        count=defaultdict(int)
8
9        for char in s:
10            count[char]+=1
11
12        for i,c in enumerate(s):
13            if count[c]==1:
14                return (i)    
15        
16        return (-1)