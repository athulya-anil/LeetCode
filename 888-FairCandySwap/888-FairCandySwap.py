# Last updated: 30/12/2025, 22:40:19
1class Solution(object):
2    def fairCandySwap(self, aliceSizes, bobSizes):
3        """
4        :type aliceSizes: List[int]
5        :type bobSizes: List[int]
6        :rtype: List[int]
7        """
8        sumA=sum(aliceSizes)
9        sumB=sum(bobSizes)
10
11        diff=(sumA-sumB)//2
12        aliceSet=set(aliceSizes)
13
14        for b in bobSizes:
15            a = b + diff
16            if a in aliceSizes:
17                return [a,b]
18
19
20
21        