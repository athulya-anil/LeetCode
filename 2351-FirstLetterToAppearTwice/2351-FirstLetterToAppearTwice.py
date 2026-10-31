# Last updated: 31/10/2026, 19:02:29
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

