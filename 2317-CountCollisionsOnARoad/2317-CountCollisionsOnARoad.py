# Last updated: 10/12/2025, 07:39:55
class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        s = directions.lstrip('L').rstrip('R')

        return sum(1 for c in s if c != 'S')