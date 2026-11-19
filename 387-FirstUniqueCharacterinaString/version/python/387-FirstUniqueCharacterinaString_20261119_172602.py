# Last updated: 19/11/2026, 17:26:02
1from collections import Counter
2class Solution:
3    def firstUniqChar(self, s: str) -> int:
4        freq=Counter(s)
5        for i, char  in enumerate(s):
6            if freq[char]==1:
7                return i
8        return -1        
9
10        