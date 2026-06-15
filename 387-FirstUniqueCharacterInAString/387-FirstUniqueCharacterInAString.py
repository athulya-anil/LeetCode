# Last updated: 14/06/2026, 23:03:23
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=defaultdict(int)

        for char in s:
            count[char]+=1

        for i,c in enumerate(s):
            if count[c]==1:
                return (i)    
        
        return (-1)