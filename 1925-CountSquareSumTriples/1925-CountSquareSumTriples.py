# Last updated: 31/10/2026, 19:03:36
class Solution(object):
    def countTriples(self, n):
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c2 = a*a + b*b
                c = int(c2**0.5)
                if c <= n and c*c == c2:
                    count += 1
        return count
