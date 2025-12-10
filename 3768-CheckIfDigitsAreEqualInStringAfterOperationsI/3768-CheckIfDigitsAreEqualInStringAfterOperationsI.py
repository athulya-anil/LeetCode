# Last updated: 10/12/2025, 07:39:34
class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_digit = (int(s[i]) + int(s[i + 1])) % 10
                new_s.append(str(new_digit))
            s = new_s

        return s[0] == s[1]







        