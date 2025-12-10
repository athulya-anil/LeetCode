# Last updated: 10/12/2025, 07:39:47
class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)

        # Step 1: compute initial power coverage
        cover = [0]*n
        prefix = [0]*(n+1)
        for i, s in enumerate(stations):
            left = max(0, i-r)
            right = min(n, i+r+1)
            prefix[left] += s
            prefix[right] -= s
        cur = 0
        for i in range(n):
            cur += prefix[i]
            cover[i] = cur

        # Step 2: feasibility check for target x
        def can(x):
            add = [0]*(n+1)
            cur = 0
            need = 0
            for i in range(n):
                cur += add[i]
                if cover[i] + cur < x:
                    diff = x - (cover[i] + cur)
                    need += diff
                    if need > k: return False
                    cur += diff
                    if i + 2*r + 1 < n:
                        add[i + 2*r + 1] -= diff
            return True

        # Step 3: binary search
        lo, hi = 0, max(cover) + k
        ans = 0
        while lo <= hi:
            mid = (lo + hi)//2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
