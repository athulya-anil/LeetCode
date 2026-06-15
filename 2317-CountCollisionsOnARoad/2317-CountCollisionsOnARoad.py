# Last updated: 14/06/2026, 23:01:33
class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        s = directions.lstrip('L').rstrip('R')

        return sum(1 for c in s if c != 'S')