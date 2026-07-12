# Last updated: 12/07/2026, 13:21:19
1class Solution(object):
2    def arrayRankTransform(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: List[int]
6        """
7        n = sorted(arr)
8        rank = {}
9        r = 1
10
11        for num in n:
12            if num not in rank:
13                rank[num] = r
14                r += 1
15        
16        for i in range(len(arr)):
17            arr[i] = rank[arr[i]]
18        
19        return arr
20        