# Last updated: 24/11/2026, 19:50:24
1from collections import Counter
2class Solution:
3    def areOccurrencesEqual(self, s: str) -> bool:
4        s=Counter(s)
5        s1=set()
6
7        for value in s.values():
8            s1.add(value)
9
10        return (True if len(s1)==1 else False)
11        