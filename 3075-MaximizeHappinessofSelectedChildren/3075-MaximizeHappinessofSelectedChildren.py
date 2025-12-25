# Last updated: 25/12/2025, 21:39:53
1class Solution(object):
2    def maximumHappinessSum(self, happiness, k):
3        """
4        :type happiness: List[int]
5        :type k: int
6        :rtype: int
7        """
8        happiness.sort(reverse=True)
9        total = 0
10
11        for i in range(k):
12            gain = happiness[i] - i
13            if gain <= 0:
14                break
15            total += gain
16
17        return total
18        