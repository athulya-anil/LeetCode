# Last updated: 24/11/2026, 20:01:02
1from collections import Counter
2class Solution:
3    def uniqueOccurrences(self, arr: list[int]) -> bool:
4        freq=Counter(arr)
5        seen=set()
6        for value in freq.values():
7            if value not in seen:
8                seen.add(value)
9            else:
10                return False    
11        return True
12        