# Last updated: 13/12/2025, 18:50:20
1import re
2
3class Solution(object):
4    def validateCoupons(self, code, businessLine, isActive):
5        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
6        order = {line: i for i, line in enumerate(valid_lines)}
7        
8        res = []
9        
10        for c, b, a in zip(code, businessLine, isActive):
11            if (
12                a and
13                b in order and
14                c and
15                re.match(r'^[A-Za-z0-9_]+$', c)
16            ):
17                res.append((order[b], c))
18        
19        res.sort()
20        return [c for _, c in res]
21