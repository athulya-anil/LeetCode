# Last updated: 31/10/2026, 19:02:36
class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        s = directions.lstrip('L').rstrip('R')

        return sum(1 for c in s if c != 'S')