# Last updated: 24/11/2026, 19:57:05
1from collections import Counter
2class Solution:
3    def areOccurrencesEqual(self, s: str) -> bool:
4        freq=Counter(s)
5        v=freq[s[0]]
6        for value in freq.values():
7            if value != v:
8                return False
9
10        return True
11        