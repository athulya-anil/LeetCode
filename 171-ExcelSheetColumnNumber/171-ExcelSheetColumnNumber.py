# Last updated: 10/07/2026, 11:59:46
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            value = (ord(char)-ord('A')+1)
            result = result*26 + value
        return result