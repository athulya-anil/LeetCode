# Last updated: 10/12/2025, 07:42:03
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return((Counter(s)) == (Counter(t)))
       