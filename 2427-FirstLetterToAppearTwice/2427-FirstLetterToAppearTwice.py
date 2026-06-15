# Last updated: 14/06/2026, 23:01:30
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = []
        for char in s:
            if char in seen:
                return char
            else:
                seen.append(char)    

