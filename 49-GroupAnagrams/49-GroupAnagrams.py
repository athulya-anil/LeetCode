# Last updated: 01/01/2026, 22:44:03
1class Solution(object):
2    def groupAnagrams(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: List[List[str]]
6        """
7        groups = defaultdict(list)
8
9        for word in strs:
10            key = tuple(sorted(word)) 
11            groups[key].append(word)
12
13        return list(groups.values())
14