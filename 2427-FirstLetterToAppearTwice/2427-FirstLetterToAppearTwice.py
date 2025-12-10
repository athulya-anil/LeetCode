# Last updated: 10/12/2025, 07:39:52
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

