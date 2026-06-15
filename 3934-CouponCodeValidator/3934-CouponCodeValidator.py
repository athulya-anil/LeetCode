# Last updated: 14/06/2026, 23:01:10
import re

class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {line: i for i, line in enumerate(valid_lines)}
        
        res = []
        
        for c, b, a in zip(code, businessLine, isActive):
            if (
                a and
                b in order and
                c and
                re.match(r'^[A-Za-z0-9_]+$', c)
            ):
                res.append((order[b], c))
        
        res.sort()
        return [c for _, c in res]
