# Last updated: 24/11/2026, 19:53:10
1from collections import Counter
2class Solution:
3    def areOccurrencesEqual(self, s: str) -> bool:
4        s=Counter(s)
5        s1=set(s.values())
6
7        return len(s1)==1
8        