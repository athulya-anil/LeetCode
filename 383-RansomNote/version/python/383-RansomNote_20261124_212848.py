# Last updated: 24/11/2026, 21:28:48
1from collections import Counter
2class Solution:
3    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
4        mag=Counter(magazine)
5
6        for char in ransomNote:
7            if char not in mag:
8                return False
9            elif mag[char]==1:
10                del mag[char]
11            else:
12                mag[char]-=1
13
14        return True                
15
16
17        