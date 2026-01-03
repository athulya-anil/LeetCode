# Last updated: 03/01/2026, 21:48:56
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        slow, fast = 0,0
8        seen = set()
9        max_length = 0
10        while fast < len(s):
11            if s[fast] not in seen:
12                seen.add(s[fast])
13                max_length = max(max_length, fast-slow+1)
14                fast +=1
15            else:
16                seen.remove(s[slow])
17                slow+=1
18        return (max_length)            
19
20        